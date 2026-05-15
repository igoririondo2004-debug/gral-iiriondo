import json
import re
import time
import ollama
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "phi3:mini"
DATASET_PATH = "dataset.jsonl"
MAX_SAMPLES = None

# 👇 NUEVO: control de rango
START_INDEX = 0
END_INDEX = 1000

PRINT_EVERY = 1

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
# DATASET
# -----------------------------
def load_dataset(path, max_samples=None):
    data = []
    bad = 0

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except:
                bad += 1

    print("❌ Bad lines:", bad)
    return data

# -----------------------------
# JSON EXTRACTION
# -----------------------------
def extract_json(text):
    if not isinstance(text, str):
        return None

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None

    try:
        return json.loads(match.group())
    except:
        return None

# -----------------------------
# VALIDATION
# -----------------------------
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

# -----------------------------
# EXACT MATCH
# -----------------------------
def exact_match(pred, expected):
    return pred == expected

# -----------------------------
# OLLAMA CALL
# -----------------------------
def query_llm(text):
    start = time.time()

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            options={
                "temperature": 0.0,
                "num_ctx": 512,
                "num_predict": 120
            }
        )

        raw = response["message"]["content"]

    except Exception as e:
        print("⚠️ Ollama error:", e)
        return "", 0.0

    return raw, time.time() - start

# -----------------------------
# EVALUATION
# -----------------------------
def evaluate(dataset):

    format_ok = 0
    rules_ok = 0
    exact_ok = 0
    latencies = []

    print(f"\n🚀 Running evaluation on {len(dataset)} samples (range {START_INDEX}-{END_INDEX})\n")

    for i, item in enumerate(tqdm(dataset)):

        raw, lat = query_llm(item["input"])
        expected = item["expected"]

        latencies.append(lat)

        parsed = extract_json(raw)

        # ---------------- DEBUG ----------------
        if i % PRINT_EVERY == 0:
            print("\n------------------------------")
            print("🧠 INPUT:", item["input"])
            print("🎯 EXPECTED:", expected)
            print("🤖 RAW:", raw)

        if parsed is None:
            print("❌ PARSED: INVALID")
            continue

        print("✅ PARSED:", parsed)
        format_ok += 1

        validated = validate(parsed)
        if validated is None:
            print("❌ RULES FAILED")
            continue

        rules_ok += 1

        if exact_match(validated, expected):
            exact_ok += 1
            print("✅ MATCH")
        else:
            print("❌ MISMATCH")

        avg_latency = sum(latencies) / len(latencies)
        throughput = (i + 1) / sum(latencies)

        print(
            f"📊 [{i+1}/{len(dataset)}] "
            f"F:{format_ok} R:{rules_ok} E:{exact_ok} "
            f"Lat:{lat:.2f}s TPS:{throughput:.2f}"
        )

        print("------------------------------")

    print("\n================ FINAL ================")
    print("Total:", len(dataset))
    print("Format:", format_ok)
    print("Rules:", rules_ok)
    print("Exact:", exact_ok)
    print("Avg latency:", round(sum(latencies) / len(latencies), 4))
    print("Throughput:", round(len(dataset) / sum(latencies), 2))
    print("======================================")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    dataset = load_dataset(DATASET_PATH, MAX_SAMPLES)

    # 👇 APLICAR RANGO AQUÍ
    dataset = dataset[START_INDEX:END_INDEX]

    print(f"Loaded: {len(dataset)} samples (from {START_INDEX} to {END_INDEX})")

    evaluate(dataset)