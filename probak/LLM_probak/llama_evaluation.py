import json
import re
import time
import os
import ollama

from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "llama3.2:3b"
DATASET_PATH = "dataset.jsonl"

BATCH_SIZE = 32
MAX_WORKERS = 4
MAX_SAMPLES = 1000   # 👈 LIMIT DATASET HERE (set None for full dataset)

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
- via no contiene goal
- via sin duplicados
- SOLO JSON
"""

# -----------------------------
# CHECK DATASET
# -----------------------------
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"Dataset no encontrado: {DATASET_PATH}")

# -----------------------------
# OLLAMA MODEL CHECK
# -----------------------------
print("🧠 Checking Ollama model...")

try:
    ollama.show(MODEL_NAME)
except Exception:
    print(f"⬇️ Pulling model '{MODEL_NAME}'...")
    ollama.pull(MODEL_NAME)

print("✅ Model ready\n")

# -----------------------------
# HELPERS
# -----------------------------
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
        pred["goal"] == expected["goal"]
        and pred["via"] == expected["via"]
    )

# -----------------------------
# LOAD DATASET
# -----------------------------
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
                data.append(json.loads(line))
            except:
                print(f"⚠️ Línea inválida {i}")

    return data


# -----------------------------
# SINGLE QUERY
# -----------------------------
def query_llm(text):

    start = time.time()

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        options={
            "temperature": 0.0,
            "top_p": 1.0,
            "seed": 42
        }
    )

    latency = time.time() - start

    return response["message"]["content"], latency


# -----------------------------
# BATCH INFERENCE
# -----------------------------
def query_llm_batch(texts):

    start_batch = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(query_llm, texts))

    batch_time = time.time() - start_batch

    raws = []
    latencies = []

    for content, latency in results:
        raws.append(content)
        latencies.append(latency)

    return raws, latencies, batch_time


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

        raws, batch_latencies, batch_time = query_llm_batch(inputs)

        total_time += batch_time

        for raw, expected, lat in zip(raws, expecteds, batch_latencies):

            latencies.append(lat)

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
    print(f"Model: {MODEL_NAME}")
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
    output_file = "ollama_llama32_results.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(
            f"""
MODEL: {MODEL_NAME}

Samples: {total}

Format valid: {format_ok}/{total} ({format_ok/total:.2%})
Rules valid: {rules_ok}/{total} ({rules_ok/total:.2%})
Exact match: {exact_ok}/{total} ({exact_ok/total:.2%})

Avg latency: {avg_latency:.4f}s
Throughput: {throughput:.2f} samples/sec
"""
        )

    print(f"💾 Saved results to {output_file}")


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    dataset = load_dataset(DATASET_PATH, MAX_SAMPLES)

    print(f"📊 Loaded {len(dataset)} samples\n")

    evaluate(dataset)