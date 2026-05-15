import os
import time
import json
import numpy as np

from vosk import Model, KaldiRecognizer
from datasets import load_from_disk


# =========================
# CONFIG
# =========================
DATASET_PATH = "subset_asr_2000/subset_2000"
MODEL_PATH = "vosk-model-small-es-0.42"

DEBUG_SAMPLES = 10  # cambia a 2000 cuando funcione


# =========================
# METRICAS
# =========================
def levenshtein(a, b):
    n, m = len(a), len(b)
    dp = np.zeros((n + 1, m + 1), dtype=int)

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )
    return dp[n][m]


def normalize(text):
    return text.lower().strip()


def wer(ref, hyp):
    ref = normalize(ref).split()
    hyp = normalize(hyp).split()

    if len(ref) == 0:
        return 1.0 if len(hyp) > 0 else 0.0

    return levenshtein(ref, hyp) / len(ref)


def cer(ref, hyp):
    ref = normalize(ref)
    hyp = normalize(hyp)

    if len(ref) == 0:
        return 1.0 if len(hyp) > 0 else 0.0

    return levenshtein(list(ref), list(hyp)) / len(ref)


# =========================
# MAIN
# =========================
print("Cargando dataset...")
ds = load_from_disk(DATASET_PATH)

ds = ds.select(range(min(DEBUG_SAMPLES, len(ds))))
print(f"DEBUG MODE: {len(ds)} ejemplos")

print("Cargando modelo Vosk...")
if not os.path.exists(MODEL_PATH):
    raise Exception(f"No existe el modelo: {MODEL_PATH}")

model = Model(MODEL_PATH)


# =========================
# EVALUACION
# =========================
wers, cers, rtfs = [], [], []
lat_init_list, lat_total_list = [], []

print(f"Evaluando {len(ds)} audios...")

for i, sample in enumerate(ds):

    # -------------------------
    # AUDIO DIRECTO (FIX CLAVE)
    # -------------------------
    audio = sample["audio"]["array"]
    sr = sample["audio"]["sampling_rate"]

    ref = sample["sentence"]

    # float32 -> int16 PCM
    audio_pcm = (audio * 32767).astype(np.int16).tobytes()

    rec = KaldiRecognizer(model, sr)

    start_time = time.time()
    first_output = None

    rec.AcceptWaveform(audio_pcm)

    result = json.loads(rec.FinalResult())
    hyp = result.get("text", "")

    end_time = time.time()

    # métricas
    w = wer(ref, hyp)
    c = cer(ref, hyp)

    audio_duration = len(audio) / sr
    rtf = (end_time - start_time) / audio_duration

    lat_init = 0  # Vosk no streaming aquí
    lat_total = end_time - start_time

    wers.append(w)
    cers.append(c)
    rtfs.append(rtf)
    lat_init_list.append(lat_init)
    lat_total_list.append(lat_total)

    print(f"[{i}] WER={w:.3f} CER={c:.3f} RTF={rtf:.3f}")


# =========================
# RESULTADOS
# =========================
report = f"""
===============================
VOSK SMALL ES 0.42
===============================

Muestras: {len(ds)}

WER medio: {np.mean(wers):.4f}
CER medio: {np.mean(cers):.4f}
RTF medio: {np.mean(rtfs):.4f}

Latencia inicial media: {np.mean(lat_init_list):.4f}s
Latencia total media: {np.mean(lat_total_list):.4f}s
"""

print(report)

with open("vosk_small_results.txt", "w") as f:
    f.write(report)

print("Guardado en vosk_small_results.txt")