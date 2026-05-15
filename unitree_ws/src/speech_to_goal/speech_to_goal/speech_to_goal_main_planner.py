import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

from speech_to_goal_interfaces.srv import LLMQuery, DetectIntent
from object_recognition_interfaces.srv import DetectObject

import math


class SpeechToGoalClient(Node):

    def __init__(self):
        super().__init__('speech_to_goal_client')

        # -----------------------------
        # STATE
        # -----------------------------
        self.busy = False
        self.current_pose = None
        self.waiting_after_arrival = False

        self.goal_tolerance = 0.2

        self.wait_timer = None
        self.post_arrival_timer = None

        # -----------------------------
        # SUBS
        # -----------------------------
        self.create_subscription(
            String,
            '/speech_text',
            self.speech_cb,
            10
        )

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_cb,
            10
        )

        # -----------------------------
        # PUB
        # -----------------------------
        self.goal_pub = self.create_publisher(
            PoseStamped,
            '/move_base_simple/goal',
            10
        )

        # -----------------------------
        # SERVICE CLIENTS
        # -----------------------------
        self.cli = self.create_client(
            LLMQuery,
            '/speech_to_goal/query_llm_waypoints'
        )

        self.intent_cli = self.create_client(
            DetectIntent,
            '/speech_to_goal/detect_intent'
        )

        self.object_cli = self.create_client(
            DetectObject,
            '/object_recognition/detect_object'
        )

        # wait for services
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando LLM service...')

        while not self.intent_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando intent service...')

        while not self.object_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando object service...')

        self.get_logger().info("SpeechToGoal CLIENT ready")

    # -------------------------------------------------
    # ODOM
    # -------------------------------------------------
    def odom_cb(self, msg):
        self.current_pose = msg.pose.pose

    # -------------------------------------------------
    # SPEECH ENTRY POINT
    # -------------------------------------------------
    def speech_cb(self, msg):

        if self.busy:
            self.get_logger().warn("Robot ocupado, ignorando comando")
            return

        text = msg.data.strip()
        if not text:
            return

        if self.current_pose is None:
            self.get_logger().warn("Sin odometría todavía")
            return

        self.get_logger().info(f"Texto recibido: {text}")

        self.busy = True

        req = DetectIntent.Request()
        req.text = text

        future = self.intent_cli.call_async(req)
        future.add_done_callback(lambda f: self.handle_intent(f, text))

    # -------------------------------------------------
    # INTENT HANDLER
    # -------------------------------------------------
    def handle_intent(self, future, original_text):

        try:
            res = future.result()
        except Exception as e:
            self.get_logger().error(f"Intent service failed: {e}")
            self.busy = False
            return

        intent = res.intent
        self.get_logger().info(f"Intent detected: {intent}")

        if intent == "noise":
            self.get_logger().warn("Orden ignorada")
            self.busy = False
            return

        if intent == "recognition":
            self.handle_recognition(original_text)
            return

        if intent == "navigation":
            self.handle_navigation(original_text)
            return

        self.get_logger().warn(f"Intent desconocido: {intent}")
        self.busy = False

    # -------------------------------------------------
    # RECOGNITION FLOW
    # -------------------------------------------------
    def handle_recognition(self, text):

        req = DetectObject.Request()
        req.text = text

        future = self.object_cli.call_async(req)
        future.add_done_callback(self.handle_object_result)

    def handle_object_result(self, future):

        try:
            res = future.result()
        except Exception as e:
            self.get_logger().error(f"Object detection failed: {e}")
            self.busy = False
            return

        self.get_logger().info(f"Objeto detectados: {res.objects}")

        self.busy = False

    # -------------------------------------------------
    # NAVIGATION FLOW
    # -------------------------------------------------
    def handle_navigation(self, text):

        req = LLMQuery.Request()
        req.query = text

        future = self.cli.call_async(req)
        future.add_done_callback(self.handle_response)

    def handle_response(self, future):

        try:
            res = future.result()
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")
            self.busy = False
            return

        if not res.success:
            self.get_logger().warn(f"LLM fallido: {res.message}")
            self.busy = False
            return

        self.get_logger().info(f"Waypoints recibidos: {len(res.waypoints)}")

        self.execute_next_waypoint(res.waypoints, 0)

    # -------------------------------------------------
    # NAVIGATION EXECUTION
    # -------------------------------------------------
    def execute_next_waypoint(self, waypoints, index):

        if index >= len(waypoints):
            self.get_logger().info("Ruta completada")
            self.busy = False
            return

        wp = waypoints[index]

        self.get_logger().info(f"Yendo a: {wp.name} ({wp.x}, {wp.y})")

        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = self.get_clock().now().to_msg()

        goal.pose.position.x = wp.x
        goal.pose.position.y = wp.y
        goal.pose.position.z = wp.z
        goal.pose.orientation.w = 1.0

        self.goal_pub.publish(goal)

        self.waiting_after_arrival = False

        if self.wait_timer:
            self.wait_timer.cancel()

        self.wait_timer = self.create_timer(
            0.2,
            lambda: self.check_arrival(wp, waypoints, index)
        )

    # -------------------------------------------------
    # ARRIVAL CHECK
    # -------------------------------------------------
    def check_arrival(self, wp, waypoints, index):

        if self.current_pose is None or self.waiting_after_arrival:
            return

        dx = self.current_pose.position.x - wp.x
        dy = self.current_pose.position.y - wp.y

        dist = math.sqrt(dx * dx + dy * dy)

        if dist < self.goal_tolerance:

            self.get_logger().info(f"Llegado a {wp.name}, esperando 2s...")

            self.waiting_after_arrival = True

            if self.wait_timer:
                self.wait_timer.cancel()

            self.post_arrival_timer = self.create_timer(
                2.0,
                lambda: self.after_pause(waypoints, index)
            )

    # -------------------------------------------------
    # PAUSE
    # -------------------------------------------------
    def after_pause(self, waypoints, index):

        if self.post_arrival_timer:
            self.post_arrival_timer.cancel()
            self.post_arrival_timer = None

        self.waiting_after_arrival = False

        self.execute_next_waypoint(waypoints, index + 1)


# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    rclpy.init()
    node = SpeechToGoalClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()