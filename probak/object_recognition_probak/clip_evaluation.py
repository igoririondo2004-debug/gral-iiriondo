import os
import time
import torch
import numpy as np
from PIL import Image
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import open_clip

# =========================
# DATASET
# =========================
DATASET_DIR = "imagenet_fisheye"

image_paths = []
true_labels = []

for root, _, files in os.walk(DATASET_DIR):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            image_paths.append(os.path.join(root, f))
            true_labels.append(os.path.basename(root))

image_paths = image_paths[:5000]
true_labels = true_labels[:5000]

print(f"Total images: {len(image_paths)}")

# =========================
# DEVICE + MODEL
# =========================
device = "cuda" if torch.cuda.is_available() else "cpu"

model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-16",
    pretrained="openai"
)

tokenizer = open_clip.get_tokenizer("ViT-B-16")

model = model.to(device)
model.eval()

# (opcional pero recomendado en 8GB)
torch.backends.cudnn.benchmark = True

# =========================
# CLASS NAMES
# =========================
class_names = sorted(list(set(true_labels)))

templates = [
    "a photo of a {}",
    "a blurry photo of a {}",
    "a close-up photo of a {}"
]

# =========================
# BUILD PROMPTS
# =========================
prompts = []
for c in class_names:
    for t in templates:
        prompts.append(t.format(c.replace("_", " ")))

text_tokens = tokenizer(prompts)

# =========================
# ENCODE TEXT (BATCHED SAFE)
# =========================
batch_size = 128
text_features_list = []

with torch.no_grad():
    for i in range(0, len(text_tokens), batch_size):
        batch = text_tokens[i:i + batch_size].to(device)

        feats = model.encode_text(batch)
        feats = feats / feats.norm(dim=-1, keepdim=True)

        text_features_list.append(feats.cpu())

text_features = torch.cat(text_features_list, dim=0)

# reshape: (classes, templates, dim)
text_features = text_features.reshape(len(class_names), len(templates), -1)
text_features = text_features.mean(dim=1)
text_features = text_features / text_features.norm(dim=-1, keepdim=True)

text_features = text_features.to(device)

# =========================
# PREDICT
# =========================
def predict(img_path):
    image = preprocess(Image.open(img_path).convert("RGB")).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)

        logits = image_features @ text_features.T
        idx = logits.argmax(dim=-1).item()

    return class_names[idx]

# =========================
# EVALUATION
# =========================
y_true = []
y_pred = []
latencies = []

for i, (img_path, label) in enumerate(tqdm(list(zip(image_paths, true_labels)))):

    start = time.time()
    pred = predict(img_path)
    end = time.time()

    latencies.append((end - start) * 1000)

    y_true.append(label)
    y_pred.append(pred)

    print(f"[{i}] {'✔' if pred == label else '✖'} {label} -> {pred}")

# =========================
# METRICS
# =========================
acc = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred, average="macro", zero_division=0)
rec = recall_score(y_true, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)

avg_latency = sum(latencies) / len(latencies)
fps = 1000 / avg_latency

print("\n================ FINAL RESULTS ================")
print(f"Top-1 Accuracy : {acc:.4f}")
print(f"Precision      : {prec:.4f}")
print(f"Recall         : {rec:.4f}")
print(f"F1-score       : {f1:.4f}")
print(f"Avg latency    : {avg_latency:.2f} ms")
print(f"Samples/sec    : {fps:.2f}")
print("==============================================")
