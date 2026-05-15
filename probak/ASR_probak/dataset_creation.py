import os
import random
import unicodedata
import re
from datasets import load_dataset

# =====================================================
# CONFIG
# =====================================================
OUTPUT_DIR = "subset_asr_2000"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Cargar train completo, mezclar y quedarnos con 50k aleatorios
RANDOM_POOL_SIZE = 50000
SEED = 42

# Distribución objetivo
DISTRIBUTION = {
    "canarias": 300,
    "centro_sur": 425,
    "norte": 550,
    "sur": 425,
    "otros": 300
}

# =====================================================
# NORMALIZAR TEXTO
# =====================================================
def normalize_text(text):
    text = str(text).lower().strip()

    # quitar tildes
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))

    # normalizar guiones
    text = text.replace("–", "-").replace("—", "-")

    # limpiar espacios múltiples
    text = re.sub(r"\s+", " ", text)

    return text

# =====================================================
# CLASIFICAR ACENTO
# =====================================================
def get_group(accent):
    accent = normalize_text(accent)

    if "islas canarias" in accent:
        return "canarias"

    elif "centro-sur peninsular" in accent or "centro sur peninsular" in accent:
        return "centro_sur"

    elif "norte peninsular" in accent:
        return "norte"

    elif "sur peninsular" in accent:
        return "sur"

    else:
        return "otros"

# =====================================================
# LOAD DATASET
# =====================================================
print("Cargando train...")

ds = load_dataset(
    "xaviviro/common_voice_es_16_1_accent",
    split="train"
)

print("Mezclando dataset...")
ds = ds.shuffle(seed=SEED)

print(f"Cogiendo muestra aleatoria de {RANDOM_POOL_SIZE} ejemplos...")
ds = ds.select(range(RANDOM_POOL_SIZE))

print("Tamaño pool:", len(ds))

# =====================================================
# AGRUPAR INDICES
# =====================================================
groups = {
    "canarias": [],
    "centro_sur": [],
    "norte": [],
    "sur": [],
    "otros": []
}

print("Analizando labels...")

for i in range(len(ds)):
    ex = ds[i]

    accent = ex["accent"]
    sentence = ex["sentence"]

    if accent is None or sentence is None:
        continue

    g = get_group(accent)
    groups[g].append(i)

# =====================================================
# MOSTRAR DISTRIBUCION
# =====================================================
print("\nDistribución real encontrada en muestra 50k:")

for g in groups:
    print(f"{g}: {len(groups[g])}")

# =====================================================
# SAMPLING FINAL
# =====================================================
selected_indices = []

for g, n in DISTRIBUTION.items():
    idxs = groups[g]
    random.seed(SEED)
    random.shuffle(idxs)

    selected = idxs[:min(n, len(idxs))]
    selected_indices.extend(selected)

    print(f"{g}: seleccionados {len(selected)}")

# =====================================================
# CREAR SUBSET
# =====================================================
subset = ds.select(selected_indices)
subset = subset.shuffle(seed=SEED)

print("\nTOTAL FINAL:", len(subset))

# =====================================================
# SAVE
# =====================================================
SAVE_PATH = os.path.join(OUTPUT_DIR, "subset_2000")
subset.save_to_disk(SAVE_PATH)

print("\nGuardado en:", SAVE_PATH)