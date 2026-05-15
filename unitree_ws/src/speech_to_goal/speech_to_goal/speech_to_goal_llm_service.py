import rclpy
from rclpy.node import Node

from visualization_msgs.msg import MarkerArray
from speech_to_goal_interfaces.srv import LLMQuery
from speech_to_goal_interfaces.msg import Waypoint

import json
import subprocess
import re
import ollama 


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
class SpeechToGoalLLM(Node):

    def __init__(self):
        super().__init__('speech_to_goal_llm')

        self.markers = {}

        # -----------------------------
        # SUBS
        # -----------------------------
        self.create_subscription(
            MarkerArray,
            '/aruco/markers_viz',
            self.marker_cb,
            10
        )

        # -----------------------------
        # SERVICE
        # -----------------------------
        self.create_service(
            LLMQuery,
            '/speech_to_goal/query_llm_waypoints',
            self.query_llm_service_callback
        )

        # -----------------------------
        # OLLAMA MODEL
        # -----------------------------
        self.MODEL_NAME = "ministral-3:3b"   # 👈 change if needed
        self.ensure_model_ready()

        self.get_logger().info("SpeechToGoal LLM (Ollama) ready")

    # -------------------------------------------------
    # MARKERS
    # -------------------------------------------------
    def marker_cb(self, msg):
        self.markers.clear()

        for m in msg.markers:
            if m.type != 9:
                continue

            name = m.text.lower().strip()
            self.markers[name] = (
                m.pose.position.x,
                m.pose.position.y
            )

    # -------------------------------------------------
    # JSON EXTRACTION
    # -------------------------------------------------
    def extract_json(self, text):
        matches = re.findall(r"\{.*?\}", text, re.DOTALL)

        for m in matches:
            try:
                return json.loads(m)
            except:
                continue

        return None

    # -------------------------------------------------
    # OLLAMA CALL (REPLACEMENT OF HF MODEL)
    # -------------------------------------------------
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
                    "content": "ve a la cocina pasando por el pasillo"
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


    def query_llm(self, user_text):

        ALLOWED_PLACES = list(self.markers.keys())

        try:
            response = ollama.chat(
                model=self.MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_text}
                ],
                options={
                    "temperature": 0.0
                }
            )

            return response["message"]["content"]

        except Exception as e:
            self.get_logger().error(f"Ollama error: {e}")
            return "{}"

    # -------------------------------------------------
    # VALIDATION (UNCHANGED)
    # -------------------------------------------------
    def validate(self, data):

        if not isinstance(data, dict):
            return None

        goal = data.get("goal")
        via = data.get("via", [])

        allowed = set(self.markers.keys())

        if goal not in allowed:
            goal = None

        via = [v for v in via if v in allowed]
        via = [v for v in via if v != goal]

        return {
            "goal": goal,
            "via": via
        }

    # -------------------------------------------------
    # SERVICE CALLBACK
    # -------------------------------------------------
    def query_llm_service_callback(self, req, res):

        raw = self.query_llm(req.query)
        self.get_logger().info(f"\nRAW:\n{raw}")

        data = self.extract_json(raw)

        if not data:
            res.success = False
            res.message = "JSON parse failed"
            res.waypoints = []
            return res

        result = self.validate(data)

        if not result or result["goal"] is None:
            self.get_logger().warn("No se han encontrado esos puntos")

            res.success = False
            res.message = "validation failed"
            res.waypoints = []
            return res

        path = result["via"] + [result["goal"]]

        waypoints = []

        for name in path:

            pose = self.markers.get(name)

            if pose is None:
                self.get_logger().warn(f"Unknown marker: {name}")
                continue

            wp = Waypoint()
            wp.name = name
            wp.x = float(pose[0])
            wp.y = float(pose[1])
            wp.z = 0.0

            waypoints.append(wp)

        res.waypoints = waypoints
        res.success = len(waypoints) > 0
        res.message = "ok"

        return res


# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    rclpy.init()
    node = SpeechToGoalLLM()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()