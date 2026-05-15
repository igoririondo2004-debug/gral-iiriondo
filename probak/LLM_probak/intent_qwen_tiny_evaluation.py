import os

# =====================================================
# FORCE CPU (MUST BE BEFORE OLLAMA IMPORT)
# =====================================================
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["OLLAMA_NUM_GPU"] = "0"

import json
import re
import time
import torch

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

# =====================================================
# CONFIG
# =====================================================
# MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
MODEL_NAME = "ministral/Ministral-3b-instruct"
DATASET_PATH = "intent_dataset.jsonl"

BATCH_SIZE = 32
MAX_SAMPLES = None

LABELS = [
    "navigation",
    "recognition",
    "noise"
]

SYSTEM_PROMPT = """
Eres un clasificador de intenciones para un robot.

Clasifica el texto del usuario en EXACTAMENTE UNA categoría:

- navigation
- recognition
- noise

Definiciones:

navigation:
Comandos relacionados con movimiento, navegación,
trayectorias, destinos o puntos intermedios.

Ejemplos:
- "ve a la cocina"
- "muévete a la silla"
- "dirígete al despacho"
- "pasa por el pasillo"
- "ve a las escaleras pasando por el garaje"

recognition:
Comandos relacionados con percepción,
reconocimiento de objetos, análisis del entorno,
descripción de escenas o actualización del mapa.

Incluye:
- describir lo que el robot ve
- detectar objetos
- reconocer elementos del entorno
- actualizar el mapa o memoria

Ejemplos:
- "¿qué tienes delante?"
- "describe la habitación"
- "detecta obstáculos"
- "reconoce los objetos delante"
- "añade esto al mapa"
- "actualiza el mapa"
- "incorpora esta información al mapa"

noise:
Texto irrelevante, ambiguo, aleatorio,
conversacional o no accionable.

Ejemplos:
- "hola"
- "repite"
- "asdfasdf"
- "hazlo"
- "espera un segundo"

Devuelve SOLO JSON válido.

Formato:
{
  "intent": "navigation"
}

Reglas:
- SOLO JSON
- Sin explicaciones
- Sin markdown
- intent debe ser exactamente uno de:
  navigation
  recognition
  noise
"""

# =====================================================
# DATASET CHECK
# =====================================================
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"Dataset not found: {DATASET_PATH}")

# =====================================================
# LOAD MODEL
# =====================================================
print("🧠 Loading model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

tokenizer.padding_side = "left"

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

model.eval()

print("✅ Model ready\n")

# =====================================================
# HELPERS
# =====================================================
def extract_json(text):

    if not isinstance(text, str):
        return None

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

    intent = data.get("intent")

    if intent not in LABELS:
        return None

    return {"intent": intent}


def exact_match(pred, expected):

    return pred["intent"] == expected


# =====================================================
# LOAD DATASET
# =====================================================
def load_dataset(path, max_samples=None):

    data = []

    with open(path, "r", encoding="utf-8") as f:

        for i, line in enumerate(f):

            if max_samples is not None and len(data) >= max_samples:
                break

            line = line.strip()

            if not line:
                continue

            try:
                item = json.loads(line)

                data.append({
                    "text": item["text"],
                    "label": item["label"]
                })

            except Exception:
                print(f"⚠️ Invalid line {i}")

    return data


# =====================================================
# BATCH INFERENCE
# =====================================================
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

    start = time.time()

    with torch.inference_mode():

        outputs = model.generate(
            **inputs,
            max_new_tokens=20,
            temperature=0.0,
            do_sample=False,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    latency = time.time() - start

    decoded = tokenizer.batch_decode(
        outputs,
        skip_special_tokens=True
    )

    cleaned = []

    for d in decoded:

        if "assistant" in d:
            d = d.split("assistant")[-1]

        cleaned.append(d)

    return cleaned, latency


# =====================================================
# EVALUATION
# =====================================================
def evaluate(dataset):

    total = len(dataset)

    format_ok = 0
    valid_ok = 0
    exact_ok = 0

    latencies = []
    total_time = 0.0

    for i in tqdm(
        range(0, total, BATCH_SIZE),
        desc="Evaluating"
    ):

        batch = dataset[i:i + BATCH_SIZE]

        texts = [x["text"] for x in batch]
        labels = [x["label"] for x in batch]

        raws, batch_latency = query_llm_batch(texts)

        total_time += batch_latency

        per_sample_latency = batch_latency / len(batch)

        for text, raw, expected in zip(texts, raws, labels):

            latencies.append(per_sample_latency)

            # -------------------------
            # JSON FORMAT
            # -------------------------
            extracted = extract_json(raw)

            if extracted is None:

                print("\n--------------------------------")
                print(f"INPUT     : {text}")
                print(f"RAW OUTPUT: {raw}")
                print("ERROR     : Invalid JSON")
                print("--------------------------------")

                continue

            format_ok += 1

            # -------------------------
            # VALID LABEL
            # -------------------------
            validated = validate(extracted)

            if validated is None:

                print("\n--------------------------------")
                print(f"INPUT     : {text}")
                print(f"RAW OUTPUT: {raw}")
                print("ERROR     : Invalid intent")
                print("--------------------------------")

                continue

            valid_ok += 1

            # -------------------------
            # EXACT MATCH
            # -------------------------
            is_correct = exact_match(validated, expected)

            if is_correct:
                exact_ok += 1

            # -------------------------
            # PRINT RESULTS
            # -------------------------
            print("\n--------------------------------")
            print(f"INPUT     : {text}")
            print(f"PREDICTED : {validated['intent']}")
            print(f"EXPECTED  : {expected}")
            print(f"CORRECT   : {is_correct}")
            print("--------------------------------")

    # =================================================
    # METRICS
    # =================================================
    avg_latency = (
        sum(latencies) / len(latencies)
        if latencies else 0.0
    )

    throughput = (
        total / total_time
        if total_time > 0 else 0.0
    )

    # =================================================
    # RESULTS
    # =================================================
    print("\n==================== RESULTS ====================")

    print(f"Model: {MODEL_NAME}")
    print(f"Total samples: {total}")

    print(
        f"Valid JSON: "
        f"{format_ok}/{total} "
        f"({format_ok/total:.2%})"
    )

    print(
        f"Valid intent: "
        f"{valid_ok}/{total} "
        f"({valid_ok/total:.2%})"
    )

    print(
        f"Exact match: "
        f"{exact_ok}/{total} "
        f"({exact_ok/total:.2%})"
    )

    print(f"Avg latency/sample: {avg_latency:.4f} s")

    print(f"Throughput: {throughput:.2f} samples/sec")

    print("================================================\n")

    # =================================================
    # SAVE RESULTS
    # =================================================
    results_text = f"""
==================== RESULTS ====================

Model: {MODEL_NAME}

Total samples: {total}

Valid JSON: {format_ok}/{total} ({format_ok/total:.2%})

Valid intent:
{valid_ok}/{total} ({valid_ok/total:.2%})

Exact match:
{exact_ok}/{total} ({exact_ok/total:.2%})

Avg latency/sample:
{avg_latency:.4f} s

Throughput:
{throughput:.2f} samples/sec

================================================
"""

    output_file = "intent_classification_qwen_tiny_results.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(results_text.strip())

    print(f"💾 Saved results to {output_file}")


# =====================================================
# MAIN
# =====================================================
if __name__ == "__main__":

    dataset = load_dataset(
        DATASET_PATH,
        MAX_SAMPLES
    )

    print(f"📊 Loaded {len(dataset)} samples\n")

    evaluate(dataset)