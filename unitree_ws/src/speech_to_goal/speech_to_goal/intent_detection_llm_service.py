import rclpy
from rclpy.node import Node
from speech_to_goal_interfaces.srv import DetectIntent
import subprocess

import ollama

LABELS = ["navigation", "recognition", "noise"]

SYSTEM_PROMPT = """
Eres un clasificador de intenciones para un robot.

Clasifica el texto del usuario en EXACTAMENTE UNA categoría:

- navigation
- recognition
- noise

Definiciones:

navigation:
Comandos relacionados con movimiento, navegación,
trayectorias, destinos o puntos intermedios.

Ejemplos:
- "ve a la cocina"
- "muévete a la silla"
- "dirígete al despacho"
- "pasa por el pasillo"
- "ve a las escaleras pasando por el garaje"

recognition:
Comandos relacionados con percepción,
reconocimiento de objetos, análisis del entorno,
descripción de escenas o actualización del mapa.

Incluye:
- describir lo que el robot ve
- detectar objetos
- reconocer elementos del entorno
- actualizar el mapa o memoria

Ejemplos:
- "¿qué tienes delante?"
- "describe la habitación"
- "detecta obstáculos"
- "reconoce los objetos delante"
- "añade esto al mapa"
- "actualiza el mapa"
- "incorpora esta información al mapa"

noise:
Texto irrelevante, ambiguo, aleatorio,
conversacional o no accionable.

Ejemplos:
- "hola"
- "repite"
- "asdfasdf"
- "hazlo"
- "espera un segundo"

Devuelve SOLO JSON válido.

Formato:
{
  "intent": "navigation"
}

Reglas:
- SOLO JSON
- Sin explicaciones
- Sin markdown
- intent debe ser exactamente uno de:
  navigation
  recognition
  noise
"""


class IntentService(Node):

    def __init__(self):
        super().__init__("intent_classifier_service")

        self.srv = self.create_service(
            DetectIntent,
            "/speech_to_goal/detect_intent",
            self.callback
        )

        self.MODEL_NAME = "ministral-3:3b"   # or mistral:7b-instruct
        self.ensure_model_ready()

        self.get_logger().info("Ollama Intent Service ready")

    def query_llm(self, text: str) -> str:

        try:
            response = ollama.chat(
                model=self.MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": text}
                ],
                options={
                    "temperature": 0.0
                }
            )

            output = response["message"]["content"].lower()

            for label in LABELS:
                if label in output:
                    return label

            return "noise"

        except Exception as e:
            self.get_logger().error(f"Ollama error: {e}")
            return "noise"

    def callback(self, request, response):

        label = self.query_llm(request.text)

        response.intent = label

        self.get_logger().info(
            f"{request.text} -> {label}"
        )

        return response
        
    def ensure_model_ready(self):

        # =====================================================
        # 1. CHECK / PULL MODEL
        # =====================================================
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True
            )

            if self.MODEL_NAME in result.stdout:
                self.get_logger().info(f"Model already installed: {self.MODEL_NAME}")
            else:
                self.get_logger().warn(f"Pulling model: {self.MODEL_NAME}")

                subprocess.run(
                    ["ollama", "pull", self.MODEL_NAME],
                    check=True
                )

                self.get_logger().info("Model pulled successfully")

        except Exception as e:
            self.get_logger().error(f"Model check/pull failed: {e}")
            return

        # =====================================================
        # 2. REALISTIC WARM-UP (CRITICAL FIX)
        # =====================================================
        try:
            self.get_logger().info("Warming up model (real prompt match)...")

            warmup_messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": "este es el warmup"
                }
            ]

            # Run multiple passes to fully stabilize runtime
            for i in range(3):
                ollama.chat(
                    model=self.MODEL_NAME,
                    messages=warmup_messages,
                    options={
                        "temperature": 0.0
                    }
                )

            self.get_logger().info("Model warm-up complete (3 realistic passes)")

        except Exception as e:
            self.get_logger().error(f"Warm-up failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = IntentService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()