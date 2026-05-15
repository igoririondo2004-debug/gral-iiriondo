import os
import cv2
import json
import random
import numpy as np
from PIL import Image
from collections import defaultdict
from pycocotools.coco import COCO

# =========================
# CONFIG
# =========================
BASE_DIR = os.path.dirname(__file__)

COCO_ANN_PATH = os.path.join(BASE_DIR, "coco/annotations/instances_val2017.json")
COCO_IMG_DIR = os.path.join(BASE_DIR, "coco/val2017")

OUTPUT_DIR = os.path.join(BASE_DIR, "fisheye_dataset")
IMG_OUT = os.path.join(OUTPUT_DIR, "images")
LABEL_FILE = os.path.join(OUTPUT_DIR, "labels.json")

TARGET_TOTAL = 5000
MAX_PER_CLASS = 500  # soft limit

os.makedirs(IMG_OUT, exist_ok=True)

# =========================
# LOAD COCO
# =========================
coco = COCO(COCO_ANN_PATH)

img_ids = coco.getImgIds()
cats = coco.loadCats(coco.getCatIds())
cat_map = {c["id"]: c["name"] for c in cats}

# =========================
# FISHEYE TRANSFORM
# =========================
def fisheye(image, strength=0.8):
    h, w = image.shape[:2]

    K = np.array([[w, 0, w / 2],
                  [0, w, h / 2],
                  [0, 0, 1]], dtype=np.float32)

    D = np.array([strength, strength, 0.0, 0.0], dtype=np.float32)

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(
        K, D, np.eye(3), K, (w, h), cv2.CV_16SC2
    )

    return cv2.remap(image, map1, map2, interpolation=cv2.INTER_LINEAR)

# =========================
# MAIN LABEL = LARGEST BBOX
# =========================
def get_main_label(img_id):
    ann_ids = coco.getAnnIds(imgIds=img_id)
    anns = coco.loadAnns(ann_ids)

    if not anns:
        return None

    best = None
    best_area = 0

    for ann in anns:
        x, y, w, h = ann["bbox"]
        area = w * h

        if area > best_area:
            best_area = area
            best = ann

    if best is None:
        return None

    return cat_map[best["category_id"]]

# =========================
# LOAD IMAGE
# =========================
def load_img(img_id):
    img_info = coco.loadImgs(img_id)[0]
    path = os.path.join(COCO_IMG_DIR, img_info["file_name"])

    try:
        img = Image.open(path).convert("RGB")
        return np.array(img), img_id
    except:
        return None, None

# =========================
# PROCESS FUNCTION
# =========================
def process(img_id):
    img, img_id_real = load_img(img_id)
    if img is None:
        return None

    label = get_main_label(img_id_real)
    if label is None:
        return None

    return img, img_id_real, label

# =========================
# BUILD DATASET
# =========================
results = []
class_count = defaultdict(int)

random.shuffle(img_ids)

# =========================
# PHASE 1: BALANCED FILL
# =========================
print("PHASE 1: balanced sampling")

for img_id in img_ids:

    if len(results) >= TARGET_TOTAL:
        break

    data = process(img_id)
    if data is None:
        continue

    img, img_id_real, label = data

    # soft balancing
    if class_count[label] >= MAX_PER_CLASS:
        continue

    distorted = fisheye(img, strength=0.8)

    filename = f"{img_id_real}.jpg"
    out_path = os.path.join(IMG_OUT, filename)

    cv2.imwrite(out_path, cv2.cvtColor(distorted, cv2.COLOR_RGB2BGR))

    results.append({
        "image_id": img_id_real,
        "file": filename,
        "label": label
    })

    class_count[label] += 1

    print(f"[{len(results)}/{TARGET_TOTAL}] {label}")

# =========================
# PHASE 2: FORCE FILL
# =========================
print("\nPHASE 2: force fill to reach exactly 5000")

i = 0
while len(results) < TARGET_TOTAL:

    img_id = img_ids[i % len(img_ids)]
    i += 1

    data = process(img_id)
    if data is None:
        continue

    img, img_id_real, label = data

    # relaxed constraint
    if class_count[label] >= MAX_PER_CLASS * 3:
        continue

    distorted = fisheye(img, strength=0.8)

    filename = f"{img_id_real}_{len(results)}.jpg"
    out_path = os.path.join(IMG_OUT, filename)

    cv2.imwrite(out_path, cv2.cvtColor(distorted, cv2.COLOR_RGB2BGR))

    results.append({
        "image_id": img_id_real,
        "file": filename,
        "label": label
    })

    class_count[label] += 1

    print(f"[{len(results)}/{TARGET_TOTAL}] {label}")

# =========================
# FINAL SAVE
# =========================
with open(LABEL_FILE, "w") as f:
    json.dump(results, f, indent=2)

print("\nDONE ✔")
print("Total images:", len(results))
print("Class distribution:")
print(dict(class_count))