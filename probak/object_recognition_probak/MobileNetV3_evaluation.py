import os
import time
import torch
from PIL import Image
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json
import urllib.request

from torchvision.models import mobilenet_v3_large, MobileNet_V3_Large_Weights

# =========================
# PATH
# =========================
DATASET_DIR = "imagenet_fisheye"

# =========================
# MODEL
# =========================
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = "cpu"  # force CPU for fair latency comparison

weights = MobileNet_V3_Large_Weights.DEFAULT
model = mobilenet_v3_large(weights=weights).to(device)
model.eval()

preprocess = weights.transforms()

idx_to_label = weights.meta["categories"]

# =========================
# 🔥 LOAD TRUE SYNSET → NAME MAP (IMPORTANT FIX)
# =========================
# This is the missing piece you never had

url = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"
data = json.loads(urllib.request.urlopen(url).read())

synset_to_name = {v[0]: v[1] for v in data.values()}

# =========================
# DATASET
# =========================
image_paths = []
true_synsets = []

for root, _, files in os.walk(DATASET_DIR):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            image_paths.append(os.path.join(root, f))
            true_synsets.append(os.path.basename(root))

image_paths = image_paths[:5000]
true_synsets = true_synsets[:5000]

print("Total images:", len(image_paths))

# =========================
# PREDICT
# =========================
def predict(img_path):
    img = Image.open(img_path).convert("RGB")
    x = preprocess(img).unsqueeze(0).to(device)

    with torch.no_grad():
        out = model(x)

    idx = torch.argmax(out, dim=1).item()
    return idx_to_label[idx]

# =========================
# NORMALIZE
# =========================
def norm(x):
    return x.replace("_", " ").lower()

# =========================
# METRICS
# =========================
y_true = []
y_pred = []
latencies = []

for i, (img_path, synset) in enumerate(tqdm(list(zip(image_paths, true_synsets)))):

    start = time.time()
    pred = predict(img_path)
    end = time.time()

    latency = (end - start) * 1000
    latencies.append(latency)

    # 🔥 CRITICAL FIX HERE
    true_label = synset_to_name.get(synset, synset)

    true_label = norm(true_label)
    pred_label = norm(pred)

    y_true.append(true_label)
    y_pred.append(pred_label)

    match = "✔" if true_label in pred_label or pred_label in true_label else "✖"

    print(f"\n[{i}] {match}")
    print(f"Expected : {true_label}")
    print(f"Predicted: {pred_label}")
    print(f"Latency  : {latency:.2f} ms")

# =========================
# RESULTS
# =========================
acc = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred, average="macro", zero_division=0)
rec = recall_score(y_true, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)

avg_latency = sum(latencies) / len(latencies)
fps = 1000 / avg_latency

print("\n================ FINAL RESULTS ================")
print(f"Top-1 Accuracy: {acc:.4f}")
print(f"Precision     : {prec:.4f}")
print(f"Recall        : {rec:.4f}")
print(f"F1-score      : {f1:.4f}")
print(f"Avg latency   : {avg_latency:.2f} ms")
print(f"Samples/sec   : {fps:.2f}")
print("==============================================")