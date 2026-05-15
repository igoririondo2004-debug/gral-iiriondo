import os
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm
import random
import shutil

# -----------------------------
# INPUT / OUTPUT
# -----------------------------
INPUT_DIR = "/home/isard/.cache/kagglehub/datasets/titericz/imagenet1k-val/versions/1"
OUTPUT_DIR = "imagenet_fisheye"
MAX_IMAGES = 5000
FISHEYE_STRENGTH = 2.0

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# FISHEYE FUNCTION
# -----------------------------
def fisheye(image, strength):
    h, w = image.shape[:2]

    K = np.array([
        [w, 0, w / 2],
        [0, w, h / 2],
        [0, 0, 1]
    ], dtype=np.float32)

    D = np.array([strength, strength, 0.0, 0.0], dtype=np.float32)

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(
        K, D, np.eye(3),
        K,
        (w, h),
        cv2.CV_16SC2
    )

    return cv2.remap(image, map1, map2, interpolation=cv2.INTER_LINEAR)

# -----------------------------
# COLLECT IMAGES (KEEP LABEL STRUCTURE)
# -----------------------------
image_paths = []

for root, _, files in os.walk(INPUT_DIR):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            full_path = os.path.join(root, f)
            label = os.path.basename(root)  # ImageNet class folder
            image_paths.append((full_path, label))

print(f"Found {len(image_paths)} images")

# shuffle for unbiased sampling
random.shuffle(image_paths)

# limit to 5000
image_paths = image_paths[:MAX_IMAGES]

# -----------------------------
# PROCESS
# -----------------------------
for i, (img_path, label) in enumerate(tqdm(image_paths)):

    try:
        img = Image.open(img_path).convert("RGB")
        img = np.array(img)

        distorted = fisheye(img, FISHEYE_STRENGTH)

        # output structure: keep label folders
        out_dir = os.path.join(OUTPUT_DIR, label)
        os.makedirs(out_dir, exist_ok=True)

        out_path = os.path.join(out_dir, f"{i:05d}.jpg")

        cv2.imwrite(
            out_path,
            cv2.cvtColor(distorted, cv2.COLOR_RGB2BGR)
        )

    except Exception as e:
        print(f"Skip {img_path}: {e}")

print("DONE ✔ Fisheye ImageNet dataset created")