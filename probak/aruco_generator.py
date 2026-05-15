import cv2
import os
import sys

# Uso:
# python3 aruco_generator.py number=10

# Valor por defecto
num_markers = 4

# Leer parámetro
for arg in sys.argv[1:]:
    if arg.startswith("number="):
        num_markers = int(arg.split("=")[1])

output_folder = "aruco_markers"
os.makedirs(output_folder, exist_ok=True)

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

for marker_id in range(num_markers):
    img = aruco.drawMarker(dictionary, marker_id, 1000)

    filename = os.path.join(output_folder, f"marker_{marker_id}.png")
    cv2.imwrite(filename, img)

print(f"{num_markers} markers saved in folder: {output_folder}")
