import json
import re
import time
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
DATASET_PATH = "dataset.jsonl"
BATCH_SIZE = 32

ALLOWED_PLACES = [
    "entrada", "pasillo", "salida",
    "sala", "salón", "comedor", "cocina", "baño",
    "dormitorio", "habitación", "oficina", "despacho",
    "estudio", "lavadero", "trastero", "garaje",
    "silla", "mesa", "escritorio", "sofá", "cama",
    "armario", "estantería", "librería", "mostrador",
    "puerta", "ventana", "pared", "columna",
    "escaleras", "ascensor", "persona"
]

SYSTEM_PROMPT = f"""
Eres un sistema de navegación de robot.

Devuelve SOLO JSON válido:

{{
  "goal": string,
  "via": [string]
}}

Reglas:
- goal y via solo pueden ser {ALLOWED_PLACES}
- via contiene puntos intermedios
- via no puede contener goal
- via sin duplicados
- solo JSON
"""

# -----------------------------
# DATASET CHECK
# -----------------------------
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"Dataset no encontrado: {DATASET_PATH}")

# -----------------------------
# MODEL LOAD
# -----------------------------
print("🧠 Loading model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# ✅ FIX: required for decoder-only models
tokenizer.padding_side = "left"

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

# model = AutoModelForCausalLM.from_pretrained(
#     MODEL_NAME,
#     device_map={"": "cpu"},   # hard force CPU placement
#     torch_dtype=torch.float32  # CPU-friendly precision
# )

model.eval()

print("✅ Model ready\n")

# -----------------------------
# HELPERS
# -----------------------------
def extract_json(text):
    matches = re.findall(r"\{.*?\}", text, re.DOTALL)
    for m in matches:
        try:
            return json.loads(m)
        except:
            continue
    return None


def validate(data):
    if not isinstance(data, dict):
        return None

    goal = data.get("goal")
    via = data.get("via", [])

    if goal not in ALLOWED_PLACES:
        return None

    via = [v for v in via if v in ALLOWED_PLACES]

    if goal in via:
        return None

    if len(via) != len(set(via)):
        return None

    return {"goal": goal, "via": via}


def exact_match(pred, expected):
    return (
        pred["goal"] == expected["goal"] and
        pred["via"] == expected["via"]
    )

# -----------------------------
# LOAD DATASET
# -----------------------------
def load_dataset(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                data.append(json.loads(line))
            except:
                print(f"⚠️ Línea inválida {i}")
    return data

# -----------------------------
# BATCH INFERENCE
# -----------------------------
def query_llm_batch(texts):
    prompts = []

    for text in texts:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]

        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        prompts.append(prompt)

    inputs = tokenizer(
        prompts,
        return_tensors="pt",
        padding=True,
        truncation=True
    ).to(model.device)

    # inputs = tokenizer(
    #     prompts,
    #     return_tensors="pt",
    #     padding=True,
    #     truncation=True
    # )

    # inputs = {k: v.to("cpu") for k, v in inputs.items()}

    start = time.time()

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=40,
            temperature=0.0,
            do_sample=False,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    latency = time.time() - start

    decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    cleaned = []
    for d in decoded:
        if "assistant" in d:
            d = d.split("assistant")[-1]
        cleaned.append(d)

    return cleaned, latency

# -----------------------------
# EVALUATION
# -----------------------------
def evaluate(dataset):

    total = len(dataset)

    format_ok = 0
    rules_ok = 0
    exact_ok = 0

    latencies = []
    total_time = 0.0

    for i in tqdm(range(0, total, BATCH_SIZE), desc="Evaluating"):

        batch = dataset[i:i + BATCH_SIZE]

        inputs = [x["input"] for x in batch]
        expecteds = [x["expected"] for x in batch]

        raws, batch_latency = query_llm_batch(inputs)

        total_time += batch_latency

        per_sample_latency = batch_latency / len(batch)

        for raw, expected in zip(raws, expecteds):

            latencies.append(per_sample_latency)

            extracted = extract_json(raw)

            if extracted is None:
                continue
            format_ok += 1

            validated = validate(extracted)
            if validated is None:
                continue
            rules_ok += 1

            if exact_match(validated, expected):
                exact_ok += 1

    # -----------------------------
    # METRICS
    # -----------------------------
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    throughput = total / total_time if total_time > 0 else 0.0

    print("\n==================== RESULTS ====================")
    print(f"Total samples: {total}")
    print(f"Format valid: {format_ok}/{total} ({format_ok/total:.2%})")
    print(f"Rules valid: {rules_ok}/{total} ({rules_ok/total:.2%})")
    print(f"Exact match: {exact_ok}/{total} ({exact_ok/total:.2%})")
    print(f"Avg latency/sample: {avg_latency:.4f} s")
    print(f"Throughput: {throughput:.2f} samples/sec")
    print("================================================\n")

    # -----------------------------
    # SAVE RESULTS
    # -----------------------------
    results_text = f"""
==================== RESULTS ====================
Total samples: {total}

Format valid: {format_ok}/{total} ({format_ok/total:.2%})
Rules valid: {rules_ok}/{total} ({rules_ok/total:.2%})
Exact match: {exact_ok}/{total} ({exact_ok/total:.2%})

Avg latency per sample: {avg_latency:.4f} s
Throughput: {throughput:.2f} samples/sec
================================================
"""

    output_file = "qwen_evaluation_results.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(results_text.strip())

    print(f"💾 Saved results to {output_file}")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    dataset = load_dataset(DATASET_PATH)
    print(f"📊 Loaded {len(dataset)} samples\n")

    evaluate(dataset)