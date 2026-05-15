import subprocess
import json
import re

MODEL = "phi3:mini"

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
- Normaliza todo a minúsculas
- Elimina palabras como: "ve a", "mueve a", "por favor", "dirígete a", "la", "al", etc.
- SOLO JSON, sin texto extra
"""

def clean_json(text):
    """Extrae JSON aunque el modelo meta texto alrededor"""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    return match.group(0)

def query_llm(text):
    prompt = SYSTEM_PROMPT + "\n\nINPUT: " + text + "\nOUTPUT:"

    result = subprocess.run(
        ["ollama", "run", MODEL, prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()

if __name__ == "__main__":
    print("🧠 Waypoint LLM test (Ollama)\n")

    while True:
        text = input("Speech> ")

        raw = query_llm(text)
        print("\nRAW OUTPUT:\n", raw)

        json_str = clean_json(raw)

        if not json_str:
            print("\n❌ No JSON detected")
            continue

        try:
            parsed = json.loads(json_str)
            print("\n✅ PARSED:")
            print(json.dumps(parsed, indent=2, ensure_ascii=False))
        except Exception as e:
            print("\n❌ JSON error:", e)