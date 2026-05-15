import time
import numpy as np
import torch
import librosa

from tqdm import tqdm
from datasets import load_from_disk
from transformers import (
    Wav2Vec2Processor,
    Wav2Vec2ForCTC
)

# =========================
# CONFIG
# =========================
DATASET_PATH = "subset_asr_2000/subset_2000"

MODEL_NAME = "jonatasgrosman/wav2vec2-large-xlsr-53-spanish"

DEBUG_SAMPLES = 2000
TARGET_SR = 16000

# =========================
# GPU
# =========================
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"🚀 Using device: {device}")

USE_FP16 = device == "cuda"

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

    audio = np.asarray(
        sample["audio"]["array"],
        dtype=np.float32
    )

    sr = sample["audio"]["sampling_rate"]

    if sr != TARGET_SR:

        audio = librosa.resample(
            audio,
            orig_sr=sr,
            target_sr=TARGET_SR
        )

    preprocessed.append({
        "audio": audio,
        "sentence": sample["sentence"]
    })


# =========================
# LOAD MODEL
# =========================
print(f"🧠 Loading model '{MODEL_NAME}'...")

processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)

model = Wav2Vec2ForCTC.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if USE_FP16 else torch.float32
)

model.to(device)
model.eval()

print("✅ Model loaded")


# =========================
# EVALUATION
# =========================
wers = []
cers = []
rtfs = []
latencies = []

print(f"\n🚀 Evaluating {len(preprocessed)} samples...\n")

for i, sample in enumerate(
    tqdm(preprocessed, desc="Evaluating")
):

    audio = sample["audio"]
    ref = sample["sentence"]

    audio_duration = len(audio) / TARGET_SR

    # =========================
    # TOKENIZATION
    # =========================
    inputs = processor(
        audio,
        sampling_rate=TARGET_SR,
        return_tensors="pt",
        padding=True
    )

    input_values = inputs.input_values.to(
        device=device,
        dtype=torch.float16 if USE_FP16 else torch.float32
    )

    # =========================
    # INFERENCE
    # =========================
    start = time.time()

    with torch.inference_mode():

        if USE_FP16:

            with torch.cuda.amp.autocast():

                logits = model(input_values).logits

        else:

            logits = model(input_values).logits

        pred_ids = torch.argmax(logits, dim=-1)

        hyp = processor.batch_decode(pred_ids)[0]

    end = time.time()

    # =========================
    # METRICS
    # =========================
    w = wer(ref, hyp)
    c = cer(ref, hyp)

    latency = end - start
    rtf = latency / audio_duration

    wers.append(w)
    cers.append(c)
    rtfs.append(rtf)
    latencies.append(latency)

    tqdm.write(
        f"[{i}] "
        f"WER={w:.3f} "
        f"CER={c:.3f} "
        f"RTF={rtf:.3f}"
    )


# =========================
# RESULTS
# =========================
report = f"""
===============================
WAV2VEC2 LARGE XLSR SPANISH
===============================

Samples: {len(preprocessed)}

WER mean: {np.mean(wers):.4f}
CER mean: {np.mean(cers):.4f}
RTF mean: {np.mean(rtfs):.4f}

Avg latency: {np.mean(latencies):.4f}s
"""

print(report)

# =========================
# SAVE RESULTS
# =========================
output_file = "wav2vec2_large_xlsr_results.txt"

with open(output_file, "w") as f:
    f.write(report)

print(f"💾 Saved to {output_file}")