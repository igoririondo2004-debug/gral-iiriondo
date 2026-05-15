import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

from speech_to_goal_interfaces.srv import LLMQuery

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
        # SERVICE CLIENT
        # -----------------------------
        self.cli = self.create_client(LLMQuery, '/speech_to_goal/query_llm_waypoints')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio LLM...')

        self.get_logger().info("SpeechToGoal CLIENT ready")

    # -------------------------------------------------
    # ODOMETRÍA
    # -------------------------------------------------
    def odom_cb(self, msg):
        self.current_pose = msg.pose.pose

    # -------------------------------------------------
    # VOZ
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

        req = LLMQuery.Request()
        req.query = text

        future = self.cli.call_async(req)
        future.add_done_callback(self.handle_response)

    # -------------------------------------------------
    # RESPUESTA LLM
    # -------------------------------------------------
    def handle_response(self, future):

        try:
            res = future.result()
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")
            self.busy = False
            return

        if not res.success:
            self.get_logger().warn(f"LLM falló: {res.message}")
            self.busy = False
            return

        self.get_logger().info(f"Waypoints recibidos: {len(res.waypoints)}")

        self.execute_next_waypoint(res.waypoints, 0)

    # -------------------------------------------------
    # NAVEGACIÓN SECUENCIAL
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

        # reset estado de llegada
        self.waiting_after_arrival = False

        # iniciar chequeo de odometría
        if self.wait_timer:
            self.wait_timer.cancel()

        self.wait_timer = self.create_timer(
            0.2,
            lambda: self.check_arrival(wp, waypoints, index)
        )

    # -------------------------------------------------
    # CHECK LLEGADA
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
    # PAUSA DE 2 SEGUNDOS
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