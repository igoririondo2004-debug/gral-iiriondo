import os

# =====================================================
# FORCE CPU (MUST BE BEFORE OLLAMA IMPORT)
# =====================================================
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["OLLAMA_NUM_GPU"] = "0"

import json
import re
import time
import ollama
import subprocess
from tqdm import tqdm

# =====================================================
# CONFIG
# =====================================================
MODEL_NAME = "llama3.2:3b"
DATASET_PATH = "intent_dataset.jsonl"

BATCH_SIZE = 32
MAX_SAMPLES = None

LABELS = ["navigation", "recognition", "noise"]

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
# DEVICE CHECK (CPU / GPU)
# =====================================================
def check_device():
    try:
        nvidia = subprocess.check_output(["nvidia-smi"], text=True).lower()

        if "ollama" in nvidia or "python" in nvidia:
            device = "GPU (active)"
        else:
            device = "GPU available but idle or CPU"

        print(f"🧠 Backend detected: {device}")
        return device

    except:
        print("🧠 Backend detected: CPU (no nvidia-smi)")
        return "CPU"


# =====================================================
# DATASET LOAD
# =====================================================
def load_dataset(path, max_samples=None):
    data = []

    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):

            if max_samples and len(data) >= max_samples:
                break

            line = line.strip()
            if not line:
                continue

            try:
                item = json.loads(line)
                data.append(item)
            except:
                print(f"⚠️ Invalid line {i}")

    return data


# =====================================================
# HELPERS
# =====================================================
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

    intent = data.get("intent")
    if intent not in LABELS:
        return None

    return {"intent": intent}


def exact_match(pred, expected):
    return pred["intent"] == expected


# =====================================================
# MODEL CALL (OLLAMA)
# =====================================================
def query_llm(text):

    start = time.time()

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        options={
            "temperature": 0.0
        }
    )

    latency = time.time() - start

    return response["message"]["content"], latency


# =====================================================
# BATCH INFERENCE
# =====================================================
def query_llm_batch(texts):

    results = []
    start_batch = time.time()

    for text in texts:
        results.append(query_llm(text))

    batch_time = time.time() - start_batch

    raws = []
    latencies = []

    for content, lat in results:
        raws.append(content)
        latencies.append(lat)

    return raws, batch_time, latencies


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

    print(f"\n🚀 Evaluating {MODEL_NAME} on {total} samples\n")

    for i in tqdm(range(0, total, BATCH_SIZE)):

        batch = dataset[i:i + BATCH_SIZE]

        texts = [x["text"] for x in batch]
        labels = [x["label"] for x in batch]

        raws, batch_time, batch_latencies = query_llm_batch(texts)

        total_time += batch_time

        for raw, expected, lat in zip(raws, labels, batch_latencies):

            latencies.append(lat)

            extracted = extract_json(raw)
            if extracted is None:
                continue
            format_ok += 1

            validated = validate(extracted)
            if validated is None:
                continue
            valid_ok += 1

            if exact_match(validated, expected):
                exact_ok += 1

    # =================================================
    # METRICS
    # =================================================
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    throughput = total / total_time if total_time > 0 else 0.0

    # =================================================
    # RESULTS
    # =================================================
    print("\n==================== RESULTS ====================")
    print(f"Model: {MODEL_NAME}")
    print(f"Total samples: {total}")

    print(f"Valid JSON: {format_ok}/{total} ({format_ok/total:.2%})")
    print(f"Valid intent: {valid_ok}/{total} ({valid_ok/total:.2%})")
    print(f"Exact match: {exact_ok}/{total} ({exact_ok/total:.2%})")

    print(f"Avg latency/sample: {avg_latency:.4f} s")
    print(f"Throughput: {throughput:.2f} samples/sec")

    print("================================================\n")


# =====================================================
# MAIN
# =====================================================
if __name__ == "__main__":

    # 🔥 DEVICE CHECK HERE
    DEVICE = check_device()
    print(f"⚙️ Running on: {DEVICE}\n")

    dataset = load_dataset(DATASET_PATH, MAX_SAMPLES)
    print(f"📊 Loaded {len(dataset)} samples\n")

    evaluate(dataset)