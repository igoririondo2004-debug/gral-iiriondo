import json
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

ALLOWED_PLACES = ["entrada", "mesa", "silla", "cocina", "pasillo"]

SYSTEM_PROMPT = f"""
Devuelve SOLO JSON válido con este formato:

{{"goal": string, "via": [string]}}

Reglas:
- goal y via solo pueden ser: {ALLOWED_PLACES}
- goal es el destino final
- via son puntos intermedios (puede ser [])
- via no puede contener goal
- via sin duplicados
- no inventes valores

Sin texto adicional.
"""


# -----------------------------
# LOAD MODEL
# -----------------------------
print("🧠 Loading model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

print("✅ Model ready\n")


# -----------------------------
# JSON EXTRACTION SAFE
# -----------------------------
def extract_json(text):
    matches = re.findall(r"\{.*?\}", text, re.DOTALL)

    for m in matches:
        try:
            return json.loads(m)
        except:
            continue

    return None


# -----------------------------
# LLM CALL (FIX REAL AQUÍ)
# -----------------------------
def query_llm(user_text):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_text}
    ]

    # 🔥 CLAVE: chat template correcto para Qwen
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=0.0,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # opcional: limpiar basura si aparece
    if "assistant" in text:
        text = text.split("assistant")[-1]

    return text


# -----------------------------
# VALIDATION
# -----------------------------
def validate(data):

    if not isinstance(data, dict):
        return None

    goal = data.get("goal")
    via = data.get("via", [])

    if goal not in ALLOWED_PLACES:
        goal = None

    via = [v for v in via if v in ALLOWED_PLACES]

    return {
        "goal": goal,
        "via": via
    }


# -----------------------------
# PIPELINE
# -----------------------------
def parse(user_text):

    raw = query_llm(user_text)

    print("\n🧾 RAW OUTPUT:\n", raw)

    data = extract_json(raw)

    if not data:
        print("❌ No valid JSON found")
        return

    result = validate(data)

    if not result:
        print("❌ Validation failed")
        return

    print("\n✅ FINAL RESULT:")
    print(json.dumps(result, indent=2, ensure_ascii=False))


# -----------------------------
# MAIN LOOP
# -----------------------------
if __name__ == "__main__":

    print("🧪 Robot Navigation LLM Test\n")

    while True:
        text = input("Speech> ")

        if text.lower() in ["exit", "quit"]:
            break

        parse(text)
