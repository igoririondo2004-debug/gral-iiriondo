import os

# -----------------------------
# FORCE CPU (MUST BE FIRST)
# -----------------------------
os.environ["OLLAMA_NUM_GPU"] = "0"
os.environ["OLLAMA_LLM_LIBRARY"] = "cpu"

import json
import re
import time
import ollama
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "gemma2:2b"
DATASET_PATH = "dataset.jsonl"

BATCH_SIZE = 32
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

            if max_samples is not None and len(data) >= max_samples:
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

    return {
        "goal": goal,
        "via": via
    }


def exact_match(pred, expected):

    return (
        pred["goal"] == expected["goal"]
        and pred["via"] == expected["via"]
    )

# -----------------------------
# QUERY MODEL (CPU)
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
            "seed": 42,
            "num_ctx": 2048,
            "num_gpu": 0
        }
    )

    latency = time.time() - start

    return response["message"]["content"], latency

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

    print(f"\n🚀 Evaluating {total} samples with {MODEL_NAME} (CPU)\n")

    for i in tqdm(range(0, total, BATCH_SIZE)):

        batch = dataset[i:i + BATCH_SIZE]

        inputs = [x["input"] for x in batch]
        expecteds = [x["expected"] for x in batch]

        start_batch = time.time()

        results = []

        for inp in inputs:
            results.append(query_llm(inp))

        total_time += time.time() - start_batch

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
    avg_latency = (
        sum(latencies) / len(latencies)
        if latencies else 0.0
    )

    throughput = (
        total / total_time
        if total_time > 0 else 0.0
    )

    print("\n==================== CPU RESULTS ====================")
    print(f"Model: {MODEL_NAME}")
    print(f"Total samples: {total}")
    print(f"Format valid: {format_ok}/{total} ({format_ok/total:.2%})")
    print(f"Rules valid: {rules_ok}/{total} ({rules_ok/total:.2%})")
    print(f"Exact match: {exact_ok}/{total} ({exact_ok/total:.2%})")
    print(f"Avg latency: {avg_latency:.4f}s")
    print(f"Throughput: {throughput:.2f} samples/sec")
    print("====================================================\n")

    # -----------------------------
    # SAVE RESULTS
    # -----------------------------
    with open("gemma2_2b_cpu_results.txt", "w") as f:
        f.write(f"""
CPU RESULTS

MODEL: {MODEL_NAME}

Samples: {total}

Format valid: {format_ok}/{total}
Rules valid: {rules_ok}/{total}
Exact match: {exact_ok}/{total}

Avg latency: {avg_latency:.4f}s
Throughput: {throughput:.2f} samples/sec
""")

    print("💾 Saved results to gemma2_2b_cpu_results.txt")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    dataset = load_dataset(DATASET_PATH, MAX_SAMPLES)

    print(f"📊 Loaded {len(dataset)} samples\n")

    evaluate(dataset)
