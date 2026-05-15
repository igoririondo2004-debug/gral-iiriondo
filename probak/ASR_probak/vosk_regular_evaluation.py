import os
import time
import zipfile
import urllib.request
import wave
import json

import numpy as np
from datasets import load_from_disk
from vosk import Model, KaldiRecognizer


# =========================
# CONFIG
# =========================
DATASET_PATH = "subset_asr_2000/subset_2000"
MODEL_NAME = "vosk-model-es-0.42"
MODEL_ZIP_URL = "https://alphacephei.com/vosk/models/vosk-model-es-0.42.zip"

NUM_SAMPLES = 10   # cambia a 2000 cuando todo funcione
SAMPLE_RATE = 16000

OUTPUT_FILE = "vosk_regular_results.txt"


# =========================
# DOWNLOAD MODEL
# =========================
def ensure_model():
    if os.path.exists(MODEL_NAME):
        print("Modelo ya existe.")
        return

    print("Descargando modelo Vosk...")
    zip_path = MODEL_NAME + ".zip"
    urllib.request.urlretrieve(MODEL_ZIP_URL, zip_path)

    print("Descomprimiendo...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(".")

    os.remove(zip_path)
    print("Modelo listo.")


# =========================
# AUDIO HELPERS
# =========================
def get_audio_array(audio_obj):
    # datasets Audio decode-safe access
    if isinstance(audio_obj, dict):
        return audio_obj["array"], audio_obj["sampling_rate"]
    return audio_obj["array"], audio_obj.sampling_rate


def array_to_pcm16(audio):
    audio = np.clip(audio, -1, 1)
    return (audio * 32767).astype(np.int16).tobytes()


# =========================
# METRICS
# =========================
def wer(ref, hyp):
    r = ref.split()
    h = hyp.split()

    dp = np.zeros((len(r) + 1, len(h) + 1))

    for i in range(len(r) + 1):
        dp[i][0] = i
    for j in range(len(h) + 1):
        dp[0][j] = j

    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            cost = 0 if r[i - 1] == h[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[len(r)][len(h)] / max(len(r), 1)


def cer(ref, hyp):
    r = list(ref)
    h = list(hyp)

    dp = np.zeros((len(r) + 1, len(h) + 1))

    for i in range(len(r) + 1):
        dp[i][0] = i
    for j in range(len(h) + 1):
        dp[0][j] = j

    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            cost = 0 if r[i - 1] == h[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[len(r)][len(h)] / max(len(r), 1)


# =========================
# LOAD DATASET
# =========================
print("Cargando dataset...")
ds = load_from_disk(DATASET_PATH)

ds = ds.shuffle(seed=42).select(range(min(NUM_SAMPLES, len(ds))))


# =========================
# LOAD MODEL
# =========================
ensure_model()
print("Cargando modelo Vosk...")
model = Model(MODEL_NAME)


# =========================
# EVALUATION
# =========================
rtfs = []
wers = []
cers = []
lat_init = []
lat_total = []

print(f"Evaluando {len(ds)} audios...")

for i, sample in enumerate(ds):
    ref = sample["sentence"]

    audio = sample["audio"]
    audio_arr, sr = get_audio_array(audio)

    pcm = array_to_pcm16(audio_arr)

    rec = KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(False)

    start_total = time.time()
    start_init = None

    rec.AcceptWaveform(pcm)
    result = json.loads(rec.FinalResult())
    hyp = result.get("text", "")

    end_total = time.time()

    # latencia inicial aproximada (Vosk no da chunk streaming aquí)
    init_latency = end_total - start_total

    w = wer(ref.lower(), hyp.lower())
    c = cer(ref.lower(), hyp.lower())

    duration = len(audio_arr) / sr
    rtf = init_latency / max(duration, 1e-6)

    rtfs.append(rtf)
    wers.append(w)
    cers.append(c)
    lat_init.append(init_latency)
    lat_total.append(init_latency)

    print(f"[{i}] RTF={rtf:.3f} WER={w:.3f} CER={c:.3f}")


# =========================
# RESULTS
# =========================
def mean(x):
    return sum(x) / len(x) if x else 0


out = f"""
===============================
VOSK ES 0.42
===============================

Muestras: {len(ds)}

RTF medio: {mean(rtfs):.4f}
WER medio: {mean(wers):.4f}
CER medio: {mean(cers):.4f}

Latencia inicial media: {mean(lat_init):.4f}s
Latencia total media: {mean(lat_total):.4f}s
"""

print(out)

with open(OUTPUT_FILE, "w") as f:
    f.write(out)

print("Guardado en", OUTPUT_FILE)
