import json
import re
import time
import os
import ollama
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "ministral-3:3b"
DATASET_PATH = "dataset.jsonl"

BATCH_SIZE = 32        # safe for GPU
MAX_WORKERS = 2        # small parallelism (GPU-safe)
MAX_SAMPLES = 1000

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
# LOAD DATASET
# -----------------------------
def load_dataset(path, max_samples=None):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if max_samples and len(data) >= max_samples:
                break
            try:
                data.append(json.loads(line))
            except:
                pass
    return data


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
        pred["goal"] == expected["goal"] and
        pred["via"] == expected["via"]
    )


# -----------------------------
# SINGLE QUERY (GPU SAFE)
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
            "num_ctx": 2048,   # GPU-friendly
        }
    )

    latency = time.time() - start

    return response["message"]["content"], latency


# -----------------------------
# EVALUATION (NO HEAVY THREADING)
# -----------------------------
def evaluate(dataset):

    total = len(dataset)

    format_ok = 0
    rules_ok = 0
    exact_ok = 0

    latencies = []
    total_time = 0.0

    print(f"\n🚀 Evaluating {total} samples on GPU...\n")

    for i in tqdm(range(0, total, BATCH_SIZE)):

        batch = dataset[i:i + BATCH_SIZE]

        inputs = [x["input"] for x in batch]
        expecteds = [x["expected"] for x in batch]

        start_batch = time.time()

        results = []
        for inp in inputs:
            results.append(query_llm(inp))

        batch_time = time.time() - start_batch
        total_time += batch_time

        for (raw, lat), expected in zip(results, expecteds):

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

    print("\n==================== GPU RESULTS ====================")
    print(f"Model: {MODEL_NAME}")
    print(f"Total samples: {total}")
    print(f"Format valid: {format_ok}/{total}")
    print(f"Rules valid: {rules_ok}/{total}")
    print(f"Exact match: {exact_ok}/{total}")
    print(f"Avg latency: {avg_latency:.4f}s")
    print(f"Throughput: {throughput:.2f} samples/sec")
    print("====================================================\n")

    with open("ollama_gpu_results.txt", "w") as f:
        f.write(f"""
MODEL: {MODEL_NAME}

Samples: {total}
Format valid: {format_ok}/{total}
Rules valid: {rules_ok}/{total}
Exact match: {exact_ok}/{total}

Avg latency: {avg_latency:.4f}s
Throughput: {throughput:.2f} samples/sec
""")


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    dataset = load_dataset(DATASET_PATH, MAX_SAMPLES)

    print(f"📊 Loaded {len(dataset)} samples (GPU MODE)\n")

    evaluate(dataset)