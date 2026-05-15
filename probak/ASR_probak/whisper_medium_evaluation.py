import time
import numpy as np
import torch
import whisper
import librosa
from tqdm import tqdm
from datasets import load_from_disk

# =========================
# CONFIG
# =========================
DATASET_PATH = "subset_asr_2000/subset_2000"
MODEL_NAME = "medium"
DEBUG_SAMPLES = 2000

TARGET_SR = 16000  # Whisper expects 16kHz

# =========================
# FORCE CPU (IMPORTANT)
# =========================
device = "cpu"
torch.set_num_threads(8)  # adjust to your CPU cores

# =========================
# METRICS
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
# LOAD DATASET
# =========================
print("📦 Loading dataset...")
ds = load_from_disk(DATASET_PATH)
ds = ds.select(range(min(DEBUG_SAMPLES, len(ds))))
print(f"DEBUG MODE: {len(ds)} samples")

# =========================
# PREPROCESS AUDIO
# =========================
print("⚡ Pre-resampling audio to 16kHz...")

preprocessed = []
for sample in tqdm(ds, desc="Resampling"):
    audio = np.asarray(sample["audio"]["array"], dtype=np.float32)
    sr = sample["audio"]["sampling_rate"]

    if sr != TARGET_SR:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=TARGET_SR)

    preprocessed.append({
        "audio": audio,
        "sentence": sample["sentence"]
    })

# =========================
# LOAD MODEL (CPU ONLY)
# =========================
print(f"🧠 Loading Whisper '{MODEL_NAME}' on CPU...")
model = whisper.load_model(MODEL_NAME, device="cpu")

# =========================
# EVALUATION
# =========================
wers, cers, rtfs, latencies = [], [], [], []

print(f"\n🚀 Evaluating {len(preprocessed)} samples...\n")

for i, sample in enumerate(tqdm(preprocessed, desc="Evaluating")):

    audio = sample["audio"]
    ref = sample["sentence"]

    audio_duration = len(audio) / TARGET_SR

    start = time.time()

    # ⚡ CPU-safe inference
    result = model.transcribe(
        audio,
        language="es",
        fp16=False,        # IMPORTANT: CPU only
        beam_size=1,
        best_of=1,
        temperature=0.0
    )

    end = time.time()

    hyp = result["text"]

    # metrics
    w = wer(ref, hyp)
    c = cer(ref, hyp)

    latency = end - start
    rtf = latency / audio_duration

    wers.append(w)
    cers.append(c)
    rtfs.append(rtf)
    latencies.append(latency)

    tqdm.write(f"[{i}] WER={w:.3f} CER={c:.3f} RTF={rtf:.3f}")


# =========================
# RESULTS
# =========================
report = f"""
===============================
WHISPER MEDIUM (CPU ONLY)
===============================

Samples: {len(preprocessed)}

WER mean: {np.mean(wers):.4f}
CER mean: {np.mean(cers):.4f}
RTF mean: {np.mean(rtfs):.4f}

Avg latency: {np.mean(latencies):.4f}s
"""

print(report)

with open("whisper_cpu_medium_results.txt", "w") as f:
    f.write(report)

print("💾 Saved to whisper_cpu_medium_results.txt")