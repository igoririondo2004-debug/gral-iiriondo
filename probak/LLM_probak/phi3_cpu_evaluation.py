import os
import json
import re
import time
import ollama
from tqdm import tqdm

# -----------------------------
# FORCE CPU
# -----------------------------
os.environ["OLLAMA_NUM_GPU"] = "0"
os.environ["OLLAMA_LLM_LIBRARY"] = "cpu"

MODEL_NAME = "phi3:mini"
DATASET_PATH = "dataset.jsonl"

PRINT_EVERY = 5

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
def load_dataset():
    data = []
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except:
                pass
    return data

# -----------------------------
def extract_json(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group())
    except:
        return None

# -----------------------------
def call_model_safe(prompt, max_retries=3):

    for attempt in range(max_retries):

        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                options={
                    "temperature": 0.0,
                    "num_ctx": 256,
                    "num_predict": 96
                }
            )

            text = response.get("message", {}).get("content", "")

            if text.strip() != "":
                return text

        except Exception as e:
            print(f"⚠ retry {attempt+1}: {e}")

        time.sleep(0.5)

    return ""

# -----------------------------
def evaluate():

    dataset = load_dataset()

    format_ok = 0
    rules_ok = 0
    exact_ok = 0

    print(f"\n🚀 Running sequential safe evaluation on {len(dataset)} samples\n")

    for i, item in enumerate(tqdm(dataset)):

        # 🔒 BLOCKING CALL (NO NEXT UNTIL DONE)
        raw = call_model_safe(item["input"])
        expected = item["expected"]

        parsed = extract_json(raw)

        if parsed:
            format_ok += 1

            goal = parsed.get("goal")
            via = parsed.get("via", [])

            if goal in ALLOWED_PLACES:
                rules_ok += 1

            if parsed == expected:
                exact_ok += 1

        # ---------------- DEBUG PRINT ----------------
        if (i + 1) % PRINT_EVERY == 0:

            print("\n------------------------------")
            print("🧠 INPUT:", item["input"])
            print("🎯 EXPECTED:", expected)
            print("🤖 RAW:", raw)
            print("📊 PROGRESS:", f"{i+1}/{len(dataset)}")
            print("------------------------------\n")

# -----------------------------
if __name__ == "__main__":
    evaluate()