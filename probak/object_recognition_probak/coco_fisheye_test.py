import cv2
import numpy as np
import requests
from PIL import Image
from io import BytesIO
import random
import matplotlib.pyplot as plt

# -----------------------------
# COCO sample image URLs (stable CDN mirrors)
# -----------------------------
COCO_IMAGES = [
    "http://images.cocodataset.org/val2017/000000039769.jpg",
    "http://images.cocodataset.org/val2017/000000022478.jpg",
    "http://images.cocodataset.org/val2017/000000061418.jpg",
    "http://images.cocodataset.org/val2017/000000005037.jpg",
    "http://images.cocodataset.org/val2017/000000082812.jpg",
]

# -----------------------------
# Download image
# -----------------------------
url = random.choice(COCO_IMAGES)
print("Downloading:", url)

response = requests.get(url, timeout=10)
img = Image.open(BytesIO(response.content)).convert("RGB")

img = np.array(img)
h, w = img.shape[:2]

# -----------------------------
# Fisheye distortion (very mild)
# -----------------------------
def fisheye_weak(image, strength=0.0008):
    h, w = image.shape[:2]

    K = np.array([[w, 0, w / 2],
                  [0, w, h / 2],
                  [0, 0, 1]], dtype=np.float32)

    D = np.array([strength, strength, 0.0, 0.0], dtype=np.float32)

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(
        K, D, np.eye(3),
        K,
        (w, h),
        cv2.CV_16SC2
    )

    return cv2.remap(image, map1, map2, interpolation=cv2.INTER_LINEAR)

# apply distortion
distorted = fisheye_weak(img, strength=2.0)  # 🔥 casi imperceptible

# -----------------------------
# Save results
# -----------------------------
Image.fromarray(img).save("original.jpg")
Image.fromarray(distorted).save("fisheye.jpg")

# -----------------------------
# Show comparison
# -----------------------------
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Fisheye (weak)")
plt.imshow(distorted)
plt.axis("off")

plt.tight_layout()
plt.show()