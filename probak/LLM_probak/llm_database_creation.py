import random
import json

# ----------------------------
# ESPACIO DE ESTADOS (LUGARES)
# ----------------------------
PLACES = [
    # --- puntos base ---
    "entrada",
    "pasillo",
    "salida",

    # --- habitaciones ---
    "sala",
    "salón",
    "comedor",
    "cocina",
    "baño",
    "dormitorio",
    "habitación",
    "oficina",
    "despacho",
    "estudio",
    "lavadero",
    "trastero",
    "garaje",

    # --- muebles / objetos ---
    "silla",
    "mesa",
    "escritorio",
    "sofá",
    "cama",
    "armario",
    "estantería",
    "librería",
    "mostrador",

    # --- estructuras ---
    "puerta",
    "ventana",
    "pared",
    "columna",
    "escaleras",
    "ascensor",

    # --- extras ---
    "persona"
]

# ----------------------------
# VERBOS VARIADOS
# ----------------------------
VERBS = [
    "ve",
    "muévete",
    "dirígete",
    "desplázate",
    "anda",
    "camina",
    "avanza",
    "navega"
]

# ----------------------------
# TEMPLATES (1 VIA)
# ----------------------------
TEMPLATES_VIA_1 = [
    "{verb} a {goal} pasando por {via}",
    "A {goal}, {verb} pasando por {via}",
    "Quiero que {verb} a {goal} pasando por {via}",
    "{verb} a {goal} vía {via}",
    "Para llegar a {goal}, {verb} pasando por {via}",
    "Tienes que {verb} hacia {goal}; antes pasa por {via}",
    "Vale, {verb} a {goal}, pero asegúrate de pasar por {via} antes"
]

# ----------------------------
# TEMPLATES (MULTI VIA)
# ----------------------------
TEMPLATES_VIA_MULTI = [
    "{verb} a {goal} pasando por {via}",
    "A {goal}, {verb} pasando por {via}",
    "Quiero que {verb} a {goal} pasando por {via}",
    "Por favor, {verb} a {goal} pasando por {via}",
    "{verb} a {goal} vía {via}",
    "Para llegar a {goal}, {verb} pasando por {via}",
    "Tienes que {verb} hacia {goal}; antes pasa por {via}",
    "Vale, {verb} a {goal}, pero pasando antes por {via}"
]

# ----------------------------
# SIN VIA
# ----------------------------
TEMPLATES_NO_VIA = [
    "{verb} a {goal}",
    "Quiero que {verb} a {goal}",
    "Para llegar a {goal}, {verb}"
]

# ----------------------------
# GENERADOR
# ----------------------------
def generate():
    start = "entrada"

    goal = random.choice([p for p in PLACES if p != start])
    verb = random.choice(VERBS)

    use_via = random.random() < 0.75

    if use_via:
        via_candidates = [p for p in PLACES if p not in [start, goal]]

        # 1 o 2 vias
        num_vias = random.choices([1, 2], weights=[0.7, 0.3])[0]
        vias = random.sample(via_candidates, k=num_vias)

        if len(vias) == 1:
            via_text = vias[0]
            template = random.choice(TEMPLATES_VIA_1)
        else:
            via_text = " y ".join(vias)
            template = random.choice(TEMPLATES_VIA_MULTI)

        text = template.format(
            verb=verb,
            goal=goal,
            via=via_text,
            start=start
        )

        return text, {
            "goal": goal,
            "via": vias
        }

    else:
        template = random.choice(TEMPLATES_NO_VIA)
        text = template.format(
            verb=verb,
            goal=goal,
            start=start
        )

        return text, {
            "goal": goal,
            "via": []
        }

# ----------------------------
# DATASET BUILDER + SAVE JSONL
# ----------------------------
def build_dataset(n=200, path="dataset.jsonl"):
    dataset = []

    for _ in range(n):
        text, label = generate()

        item = {
            "input": text,
            "expected": label
        }

        dataset.append(item)

    # guardar JSONL
    with open(path, "w", encoding="utf-8") as f:
        for item in dataset:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    return dataset

# ----------------------------
# TEST
# ----------------------------
if __name__ == "__main__":
    data = build_dataset(1000)

    for d in data:
        print(d["input"])
        print(d["expected"])
        print("---")