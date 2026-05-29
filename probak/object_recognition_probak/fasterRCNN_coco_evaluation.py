import os
import time
import torch
from tqdm import tqdm
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from pycocotools.coco import COCO
import torchvision
from torchvision.transforms import functional as F

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
device = torch.device("cpu")  # or "cuda"

# ======================================
# MODEL (Faster R-CNN pretrained COCO)
# ======================================
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
    weights="DEFAULT"
)
model.to(device)
model.eval()

# COCO loader
coco = COCO(COCO_ANN_PATH)

cat_id_to_name = {
    cat["id"]: cat["name"]
    for cat in coco.loadCats(coco.getCatIds())
}

img_ids = coco.getImgIds()[:5000]

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
    img = torchvision.io.read_image(img_path).float() / 255.0

    img = img.to(device)

    with torch.no_grad():
        outputs = model([img])[0]

    if len(outputs["boxes"]) == 0:
        return "no detection"

    # best confidence
    scores = outputs["scores"].cpu().numpy()
    best_idx = scores.argmax()

    cls_id = int(outputs["labels"][best_idx].item())

    # COCO category id is same as label index mapping in torchvision model
    return coco.cats[cls_id]["name"]

# ======================================
# EVALUATION
# ======================================
y_true, y_pred, latencies = [], [], []

for i, img_id in enumerate(tqdm(img_ids)):

    img_info = coco.loadImgs(img_id)[0]
    img_path = os.path.join(COCO_IMG_DIR, img_info["file_name"])

    ann_ids = coco.getAnnIds(imgIds=img_id)
    anns = coco.loadAnns(ann_ids)

    if len(anns) == 0:
        continue

    # largest object
    largest_ann = max(anns, key=lambda x: x["area"])
    true_cat_id = largest_ann["category_id"]
    true_label = cat_id_to_name[true_cat_id]

    start = time.time()
    pred_label = predict(img_path)
    end = time.time()

    latencies.append((end - start) * 1000)

    true_label = norm(true_label)
    pred_label = norm(pred_label)

    y_true.append(true_label)
    y_pred.append(pred_label)

    print(f"[{i}] {true_label} -> {pred_label}")

# ======================================
# METRICS
# ======================================
acc = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred, average="macro", zero_division=0)
rec = recall_score(y_true, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)

avg_latency = sum(latencies) / len(latencies)
fps = 1000 / avg_latency

print("\n================ FINAL RESULTS ================")
print(f"Accuracy   : {acc:.4f}")
print(f"Precision  : {prec:.4f}")
print(f"Recall     : {rec:.4f}")
print(f"F1-score   : {f1:.4f}")
print(f"Latency ms : {avg_latency:.2f}")
print(f"FPS        : {fps:.2f}")
print("==============================================")
