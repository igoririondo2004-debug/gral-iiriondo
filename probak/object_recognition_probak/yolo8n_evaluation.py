import os
import time
import json
import torch
from PIL import Image
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import urllib.request

from ultralytics import YOLO

# =========================
# PATH
# =========================
DATASET_DIR = "imagenet_fisheye"

# =========================
# DEVICE
# =========================
device = "cuda"  # force CPU

# =========================
# MODEL (YOLOv8n DETECTION)
# =========================
model = YOLO("yolov8n.pt")  # detection model

# COCO class labels
idx_to_label = model.names

# =========================
# ImageNet synset → name mapping
# =========================
url = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"
data = json.loads(urllib.request.urlopen(url).read())

synset_to_name = {v[0]: v[1] for v in data.values()}

# =========================
# LOAD DATASET
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

print(f"Total images: {len(image_paths)}")

# =========================
# NORMALIZATION
# =========================
def norm(x):
    return x.replace("_", " ").lower().strip()

# =========================
# PREDICTION (YOLOv8 detection)
# =========================
def predict(img_path):

    results = model.predict(
        img_path,
        device=device,
        verbose=False
    )

    r = results[0]

    # no detections
    if len(r.boxes) == 0:
        return "no detection"

    # highest confidence detection
    confs = r.boxes.conf.cpu().numpy()
    best_idx = confs.argmax()

    cls_id = int(r.boxes.cls[best_idx].item())

    return idx_to_label[cls_id]

# =========================
# METRICS
# =========================
y_true = []
y_pred = []
latencies = []

for i, (img_path, synset) in enumerate(tqdm(list(zip(image_paths, true_synsets)))):

    start = time.time()
    pred_label = predict(img_path)
    end = time.time()

    latency = (end - start) * 1000
    latencies.append(latency)

    # convert synset → human label
    true_label = synset_to_name.get(synset, synset)

    # normalize
    true_label = norm(true_label)
    pred_label = norm(pred_label)

    y_true.append(true_label)
    y_pred.append(pred_label)

    match = "✔" if true_label == pred_label else "✖"

    print(f"\n[{i}] {match}")
    print(f"Expected : {true_label}")
    print(f"Predicted: {pred_label}")
    print(f"Latency  : {latency:.2f} ms")

# =========================
# FINAL RESULTS
# =========================
acc = accuracy_score(y_true, y_pred)

prec = precision_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

rec = recall_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

f1 = f1_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

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
