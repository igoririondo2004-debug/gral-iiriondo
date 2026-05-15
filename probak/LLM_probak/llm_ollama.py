import requests
import json
import re

MODEL = "qwen2.5:0.5b"  # o phi3:mini si quieres más velocidad

# 👉 TU MAPA REAL (CLAVE)
ALLOWED_PLACES = ["entrada", "mesa", "silla", "cocina", "pasillo"]

SYSTEM_PROMPT = f"""
Eres un sistema determinista de navegación de robot.

Tu tarea es extraer estructura en formato JSON estricto.

RESPUESTA OBLIGATORIA:
Devuelve SOLO un JSON válido. No texto, no markdown, no explicaciones.

FORMATO EXACTO:
{{
  "goal": string,
  "via": [string]
}}

REGLAS ESTRICTAS DE TIPOS:
- goal DEBE ser EXACTAMENTE un string
- via DEBE ser una lista de strings (puede ser [])
- NUNCA uses listas para "goal"
- NUNCA uses strings para "via"

REGLAS DE VALORES:
- Todos los valores deben estar en:
{ALLOWED_PLACES}

REGLAS SEMÁNTICAS:
- goal es el destino FINAL y único
- via contiene SOLO puntos intermedios
- via NO puede contener goal
- via puede estar vacía si no hay intermediarios

REGLAS CRÍTICAS (OBLIGATORIAS):
- Si hay múltiples posibles goals en la frase, elige SOLO UNO
- Si hay ambigüedad, selecciona el más cercano al final de la instrucción
- No inventes lugares fuera de la lista permitida
- No agrupes goals

SALIDA:
- SOLO JSON
- SIN ``` ni texto adicional
"""
 

def clean_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    return match.group(0)

def query_llm(text):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        "stream": False,
        "options": {
            "temperature": 0,
            "num_predict": 80
        }
    }

    r = requests.post(url, json=payload)
    r.raise_for_status()

    return r.json()["message"]["content"]

def parse(text):
    raw = query_llm(text)
    print("\nRAW:\n", raw)

    json_str = clean_json(raw)
    if not json_str:
        return None

    data = json.loads(json_str)

    # 🔒 HARD SAFETY FILTER (IMPORTANTE)
    if data.get("goal") not in ALLOWED_PLACES:
        data["goal"] = None

    data["via"] = [v for v in data.get("via", []) if v in ALLOWED_PLACES]

    return data


if __name__ == "__main__":
    print("🧠 Robot parser (goal + via safe)\n")

    while True:
        text = input("Speech> ")
        result = parse(text)
        print("\n✅ RESULT:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
