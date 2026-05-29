import os
import time
import json
import torch
from tqdm import tqdm
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from ultralytics import YOLO
from pycocotools.coco import COCO

# ======================================
# PATHS
# ======================================
BASE_DIR = "."

COCO_ANN_PATH = os.path.join(
    BASE_DIR,
    "coco/annotations/instances_val2017.json"
)

COCO_IMG_DIR = os.path.join(
    BASE_DIR,
    "coco/val2017"
)

# ======================================
# DEVICE
# ======================================
device = "cuda"   # force CPU

# ======================================
# MODEL
# ======================================
model = YOLO("yolov8n.pt")

# YOLO class names
idx_to_label = model.names

# ======================================
# LOAD COCO
# ======================================
coco = COCO(COCO_ANN_PATH)

# category id -> category name
cat_id_to_name = {
    cat["id"]: cat["name"]
    for cat in coco.loadCats(coco.getCatIds())
}

# image ids
img_ids = coco.getImgIds()

# limit samples
img_ids = img_ids[:5000]

print(f"Total images: {len(img_ids)}")

# ======================================
# NORMALIZATION
# ======================================
def norm(x):
    return x.replace("_", " ").lower().strip()

# ======================================
# PREDICTION
# ======================================
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

    # best confidence box
    confs = r.boxes.conf.cpu().numpy()
    best_idx = confs.argmax()

    cls_id = int(r.boxes.cls[best_idx].item())

    return idx_to_label[cls_id]

# ======================================
# EVALUATION
# ======================================
y_true = []
y_pred = []
latencies = []

for i, img_id in enumerate(tqdm(img_ids)):

    # image info
    img_info = coco.loadImgs(img_id)[0]

    img_path = os.path.join(
        COCO_IMG_DIR,
        img_info["file_name"]
    )

    # annotations for image
    ann_ids = coco.getAnnIds(imgIds=img_id)
    anns = coco.loadAnns(ann_ids)

    # skip images with no annotations
    if len(anns) == 0:
        continue

    # choose largest object as GT
    largest_ann = max(
        anns,
        key=lambda x: x["area"]
    )

    true_cat_id = largest_ann["category_id"]
    true_label = cat_id_to_name[true_cat_id]

    # inference
    start = time.time()

    pred_label = predict(img_path)

    end = time.time()

    latency = (end - start) * 1000
    latencies.append(latency)

    # normalize
    true_label = norm(true_label)
    pred_label = norm(pred_label)

    y_true.append(true_label)
    y_pred.append(pred_label)

    match = "✔" if true_label == pred_label else "✖"

    print(f"\n[{i}] {match}")
    print(f"Image     : {img_info['file_name']}")
    print(f"Expected  : {true_label}")
    print(f"Predicted : {pred_label}")
    print(f"Latency   : {latency:.2f} ms")

# ======================================
# FINAL METRICS
# ======================================
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
