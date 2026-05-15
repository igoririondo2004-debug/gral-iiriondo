import os
import time
import torch
from PIL import Image
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from ultralytics import YOLO

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

print("Total images:", len(image_paths))

# =========================
# MODEL (YOLOv8)
# =========================
model = YOLO("yolov8n.pt")  # small + fast

# COCO class names
class_names = model.names

# =========================
# PREDICT FUNCTION
# =========================
def predict(img_path):
    results = model(img_path, verbose=False)[0]

    if len(results.boxes) == 0:
        return "none"

    # take highest confidence detection
    confs = results.boxes.conf.cpu().numpy()
    cls_ids = results.boxes.cls.cpu().numpy()

    best_idx = confs.argmax()
    cls_id = int(cls_ids[best_idx])

    return class_names[cls_id]

# =========================
# METRICS
# =========================
y_true = []
y_pred = []
latencies = []

for i, (img_path, label) in enumerate(tqdm(list(zip(image_paths, true_labels)))):

    start = time.time()
    pred = predict(img_path)
    end = time.time()

    latency = (end - start) * 1000
    latencies.append(latency)

    y_true.append(label)
    y_pred.append(pred)

    match = "✔" if label in pred or pred in label else "✖"

    print(f"\n[{i}] {match}")
    print("Expected :", label)
    print("Predicted:", pred)
    print("Latency  :", f"{latency:.2f} ms")

# =========================
# FINAL RESULTS
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