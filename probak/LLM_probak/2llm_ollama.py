import ollama
import json
import re

MODEL = "phi3:mini"

# 🔥 MUY IMPORTANTE: vocabulario cerrado del robot
SYSTEM_PROMPT = """
Eres un sistema de navegación para un robot móvil.

Tu tarea es convertir instrucciones en lenguaje natural a JSON estricto.

RESPONDE SOLO CON JSON VÁLIDO.

Formato obligatorio:
{
  "intent": "navigate" | "none",
  "goal": string or null,
  "via": [lista de strings]
}

Reglas importantes:
- Si el usuario da una orden de movimiento -> intent = "navigate"
- Si no es movimiento -> intent = "none"
- goal = destino final
- via = puntos intermedios (ordenados)
- Si no hay intermediarios -> via = []
- SOLO JSON, sin texto extra
"""

# -----------------------------
# EXTRAER JSON LIMPIO
# -----------------------------
def extract_json(text: str):
    text = text.strip()

    # elimina ```json ... ```
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # busca primer bloque JSON
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None

    return match.group(0)

# -----------------------------
# LLAMADA OLLAMA
# -----------------------------
def query_llm(text: str):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        options={
            "temperature": 0,
            "num_predict": 64
        }
    )

    return response["message"]["content"]

# -----------------------------
# PARSER
# -----------------------------
def parse(text: str):
    raw = query_llm(text)
    print("\nRAW:\n", raw)

    json_str = extract_json(raw)

    if not json_str:
        print("❌ No JSON encontrado")
        return None

    try:
        return json.loads(json_str)
    except Exception as e:
        print("❌ JSON inválido:", e)
        return None

# -----------------------------
# MAIN LOOP
# -----------------------------
if __name__ == "__main__":
    print("🧠 Fast Robot Waypoint Parser (Ollama + phi3:mini)\n")

    while True:
        text = input("Speech> ")

        result = parse(text)

        print("\nPARSED:\n", result)
