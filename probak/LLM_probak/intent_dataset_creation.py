import json
import random

INPUT_FILE = "dataset.jsonl"
OUTPUT_FILE = "intent_dataset.jsonl"
N_SAMPLES = 300

# -----------------------------
# DISTRIBUTION
# -----------------------------
WAYPOINT_RATIO = 0.4
RECOGNITION_RATIO = 0.4
NOISE_RATIO = 0.2


# -----------------------------
# LOAD DATASET
# -----------------------------
def load_dataset(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


# -----------------------------
# WAYPOINTS DATA
# -----------------------------
WAYPOINT_TEMPLATES = [
    # solo ejemplos fallback si dataset falla
]


# -----------------------------
# BASE (VISION / OBJECT)
# -----------------------------
BASE_TEMPLATES = [
    "¿Qué tienes delante?",
    "¿Qué estás viendo ahora?",
    "Dime qué tienes delante",
    "Describe lo que ves delante",
    "¿Qué hay en frente del robot?",
    "¿Qué objetos hay delante?",
    "Detecta los objetos delante de ti",
    "Identifica lo que tienes delante",
    "Reconoce los objetos que tienes delante",
    "¿Qué objetos puedes ver aquí?",
    "Analiza lo que hay delante",
    "Detecta lo que tienes delante"
]

# -----------------------------
# MAPPING (SLAM / MEMORY)
# -----------------------------
MAPPING_TEMPLATES = [
    "Añade lo que ves al mapa",
    "Actualiza el mapa con lo que tienes delante",
    "Registra esta escena en el mapa",
    "Guarda lo que ves en el mapa",
    "Incorpora esta información al mapa",
    "Mapea lo que estás viendo ahora",
]


# -----------------------------
# NOISE
# -----------------------------
NOISE_TEMPLATES = [
    "ok", "vale", "hazlo", "sí", "no", "mmm", "repite",
    "no entiendo", "¿eh?", "está bien", "continúa",
    "para", "stop", "ok entendido", "de acuerdo"
]

NOISE_SENTENCES = [
    "no sé qué está pasando",
    "esto no funciona",
    "espera un segundo",
    "creo que hay un error",
    "no entiendo nada",
    "haz lo que quieras",
    "vale sigue",
    "ok hazlo",
    "olvídalo",
    "el sistema está respondiendo lento hoy",
    "esto parece incorrecto",
]


# -----------------------------
# CLEAN TEXT (NO FINAL DOT EVER)
# -----------------------------
def clean(text):
    text = text.strip()
    if text.endswith("."):
        text = text[:-1]
    return text


# -----------------------------
# JOIN BASE + MAPPING
# -----------------------------
def join(base, mapping):
    base = base.strip()
    mapping = mapping.strip()

    if base.endswith("?"):
        return f"{base} {mapping}"
    else:
        return f"{base}. {mapping}"


# -----------------------------
# RECOGNITION BUILDER
# -----------------------------
def build_recognition(n):

    samples = []

    for _ in range(n):

        r = random.random()

        if r < 0.45:
            mode = "base"
        elif r < 0.70:   # 0.45 + 0.25
            mode = "mapping"
        else:
            mode = "combined"

        if mode == "base":
            text = random.choice(BASE_TEMPLATES)

        elif mode == "mapping":
            text = random.choice(MAPPING_TEMPLATES)

        else:
            text = join(
                random.choice(BASE_TEMPLATES),
                random.choice(MAPPING_TEMPLATES)
            )

        text = clean(text)

        samples.append({
            "text": text,
            "label": "recognition"
        })

    return samples


# -----------------------------
# WAYPOINTS
# -----------------------------
def build_waypoints(dataset, n):
    samples = [
        {"text": item["input"], "label": "waypoints"}
        for item in dataset
    ]
    return random.sample(samples, min(n, len(samples)))


# -----------------------------
# NOISE
# -----------------------------
def build_noise(n):

    samples = []

    for _ in range(n):

        if random.random() < 0.5:
            text = random.choice(NOISE_TEMPLATES)
        else:
            text = random.choice(NOISE_SENTENCES)

        text = clean(text)

        samples.append({
            "text": text,
            "label": "noise"
        })

    return samples


# -----------------------------
# MAIN
# -----------------------------
def main():

    dataset = load_dataset(INPUT_FILE)

    n_waypoints = int(N_SAMPLES * WAYPOINT_RATIO)
    n_recognition = int(N_SAMPLES * RECOGNITION_RATIO)
    n_noise = N_SAMPLES - n_waypoints - n_recognition

    waypoints = build_waypoints(dataset, n_waypoints)
    recognition = build_recognition(n_recognition)
    noise = build_noise(n_noise)

    final = waypoints + recognition + noise
    random.shuffle(final)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for item in final:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print("✅ Dataset creado correctamente")
    print(f"Total: {len(final)}")
    print(f"waypoints: {sum(1 for x in final if x['label']=='waypoints')}")
    print(f"recognition: {sum(1 for x in final if x['label']=='recognition')}")
    print(f"noise: {sum(1 for x in final if x['label']=='noise')}")


if __name__ == "__main__":
    main()