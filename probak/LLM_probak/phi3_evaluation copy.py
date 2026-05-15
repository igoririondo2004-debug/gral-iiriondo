import json
import re
import time
import ollama
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "phi3:mini"   # 👈 Phi-3 Mini
DATASET_PATH = "dataset.jsonl"

BATCH_SIZE = 1
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
# DATASET
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
# PARSING
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
    return pred["goal"] == expected["goal"] and pred["via"] == expected["via"]

# -----------------------------
# MODEL CALL (GPU)
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
            "num_ctx": 512
        }
    )

    return response["message"]["content"], time.time() - start

# -----------------------------
# EVALUATION
# -----------------------------
def evaluate(dataset):

    total = len(dataset)

    format_ok = 0
    rules_ok = 0
    exact_ok = 0
    latencies = []
    total_time = 0

    print(f"\n🚀 Running {MODEL_NAME} on {total} samples\n")

    for i in tqdm(range(0, total, BATCH_SIZE)):

        batch = dataset[i:i+BATCH_SIZE]

        inputs = [x["input"] for x in batch]
        expecteds = [x["expected"] for x in batch]

        start_batch = time.time()

        results = [query_llm(inp) for inp in inputs]

        batch_time = time.time() - start_batch
        total_time += batch_time

        for (raw, lat), exp in zip(results, expecteds):

            latencies.append(lat)

            parsed = extract_json(raw)
            if not parsed:
                continue
            format_ok += 1

            parsed = validate(parsed)
            if not parsed:
                continue
            rules_ok += 1

            if exact_match(parsed, exp):
                exact_ok += 1

        # -----------------------------
        # 📊 METRICS AFTER EACH BATCH
        # -----------------------------
        processed = min(i + BATCH_SIZE, total)

        avg_latency = sum(latencies) / len(latencies) if latencies else 0
        throughput = processed / total_time if total_time > 0 else 0

        print(
            f"\n📦 Batch {i//BATCH_SIZE + 1} | "
            f"Processed: {processed}/{total} | "
            f"Format: {format_ok} | "
            f"Rules: {rules_ok} | "
            f"Exact: {exact_ok} | "
            f"Avg latency: {avg_latency:.3f}s | "
            f"Throughput: {throughput:.2f} req/s"
        )

    print("\n==================== RESULTS ====================")
    print("Model:", MODEL_NAME)
    print("Total:", total)
    print("Format:", format_ok)
    print("Rules:", rules_ok)
    print("Exact:", exact_ok)
    print("Avg latency:", round(sum(latencies) / len(latencies), 4))
    print("Throughput:", round(total / total_time, 2))
    print("=================================================\n")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    dataset = load_dataset(DATASET_PATH, MAX_SAMPLES)
    print("Loaded:", len(dataset))

    evaluate(dataset)
