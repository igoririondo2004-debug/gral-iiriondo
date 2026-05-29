import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

from speech_to_goal_interfaces.srv import LLMQuery, DetectIntent
from object_recognition_interfaces.srv import DetectObject
from ament_index_python.packages import get_package_share_directory

import math
import os

from datetime import datetime


class SpeechToGoalClient(Node):

    def __init__(self):
        super().__init__('speech_to_goal_client')
        # -----------------------------
        # LOG FILE (WORKSPACE + SRC)
        # -----------------------------
        workspace_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', '..')
        )

        results_dir = os.path.join(
            workspace_dir,
            'src',
            'speech_to_goal',
            'results'
        )

        os.makedirs(results_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.log_file_path = os.path.join(
            results_dir,
            f'navigation_log_{timestamp}.txt'
        )

        self.get_logger().info(
            f"Saving logs to: {self.log_file_path}"
        )

        # -----------------------------
        # STATE
        # -----------------------------
        self.declare_parameter("map_name", "tknika_proba_handia")
        self.map_name = self.get_parameter("map_name").value

        self.busy = False
        self.current_pose = None
        self.waiting_after_arrival = False

        self.goal_tolerance = 0.3

        self.wait_timer = None
        self.post_arrival_timer = None

        # -----------------------------
        # NAVIGATION METRICS
        # -----------------------------
        self.navigation_start_time = None
        self.total_distance = 0.0

        self.waypoint_start_time = None
        self.current_waypoint_distance = 0.0

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

        self.aruco_map_pub = self.create_publisher(
            String,
            '/aruco/load_map',
            10
        )

        self.mapping_map_pub = self.create_publisher(
            String,
            '/mapping/load_map',
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

        # -----------------------------
        # WAIT FOR SERVICES
        # -----------------------------
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Esperando LLM service...'
            )

        while not self.intent_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Esperando intent service...'
            )

        while not self.object_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Esperando object service...'
            )


        self.load_maps()
        
        self.get_logger().info(
            "SpeechToGoal CLIENT ready"
        )


    # -------------------------------------------------
    # CUSTOM LOGGER
    # -------------------------------------------------
    def log_and_save(self, text):

        # ROS logger
        self.get_logger().info(text)

        # save to txt
        with open(self.log_file_path, 'a') as f:
            f.write(text + '\n')

    # -------------------------------------------------
    # LOADING MAPS
    # -------------------------------------------------
    def load_maps(self):
        msg = String()
        msg.data = self.map_name

        self.aruco_map_pub.publish(msg)
        self.mapping_map_pub.publish(msg)

        self.get_logger().info(
            f"Requested map load: {self.map_name}"
        )

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
            self.get_logger().warn(
                "Robot ocupado, ignorando comando"
            )
            return

        text = msg.data.strip()

        if not text:
            return

        if self.current_pose is None:
            self.get_logger().warn(
                "Sin odometría todavía"
            )
            return

        self.log_and_save(
            f"Texto recibido: {text}"
        )

        self.busy = True

        req = DetectIntent.Request()
        req.text = text

        future = self.intent_cli.call_async(req)

        future.add_done_callback(
            lambda f: self.handle_intent(
                f,
                text
            )
        )

    # -------------------------------------------------
    # INTENT HANDLER
    # -------------------------------------------------
    def handle_intent(
        self,
        future,
        original_text
    ):

        try:
            res = future.result()

        except Exception as e:

            self.get_logger().error(
                f"Intent service failed: {e}"
            )

            self.busy = False
            return

        intent = res.intent

        self.log_and_save(
            f"Intent detected: {intent}"
        )

        if intent == "noise":

            self.get_logger().warn(
                "Orden ignorada"
            )

            self.busy = False
            return

        if intent == "recognition":
            self.handle_recognition(
                original_text
            )
            return

        if intent == "navigation":
            self.handle_navigation(
                original_text
            )
            return

        self.get_logger().warn(
            f"Intent desconocido: {intent}"
        )

        self.busy = False

    # -------------------------------------------------
    # RECOGNITION FLOW
    # -------------------------------------------------
    def handle_recognition(self, text):

        req = DetectObject.Request()
        req.text = text

        future = self.object_cli.call_async(req)

        future.add_done_callback(
            self.handle_object_result
        )

    def handle_object_result(self, future):

        try:
            res = future.result()

        except Exception as e:

            self.get_logger().error(
                f"Object detection failed: {e}"
            )

            self.busy = False
            return

        self.log_and_save(
            f"Objetos detectados: {res.objects}"
        )

        self.busy = False

    # -------------------------------------------------
    # NAVIGATION FLOW
    # -------------------------------------------------
    def handle_navigation(self, text):

        req = LLMQuery.Request()
        req.query = text

        future = self.cli.call_async(req)

        future.add_done_callback(
            self.handle_response
        )

    def handle_response(self, future):

        try:
            res = future.result()

        except Exception as e:

            self.get_logger().error(
                f"Service call failed: {e}"
            )

            self.busy = False
            return

        if not res.success:

            self.get_logger().warn(
                f"LLM fallido: {res.message}"
            )

            self.busy = False
            return

        self.log_and_save(
            f"Waypoints recibidos: "
            f"{len(res.waypoints)}"
        )

        # -----------------------------
        # RESET METRICS
        # -----------------------------
        self.navigation_start_time = (
            self.get_clock().now()
        )

        self.total_distance = 0.0

        # -----------------------------
        # COMPUTE CHAINED DISTANCES
        # -----------------------------
        prev_x = self.current_pose.position.x
        prev_y = self.current_pose.position.y

        for i, wp in enumerate(res.waypoints):

            dx = wp.x - prev_x
            dy = wp.y - prev_y

            dist = math.sqrt(
                dx * dx + dy * dy
            )

            self.total_distance += dist

            # first waypoint
            if i == 0:

                self.log_and_save(
                    f"Distancia robot -> "
                    f"{wp.name}: "
                    f"{dist:.2f} metros"
                )

            # chained waypoints
            else:

                prev_wp = res.waypoints[i - 1]

                self.log_and_save(
                    f"Distancia "
                    f"{prev_wp.name} -> "
                    f"{wp.name}: "
                    f"{dist:.2f} metros"
                )

            prev_x = wp.x
            prev_y = wp.y

        self.log_and_save(
            f"Distancia total estimada: "
            f"{self.total_distance:.2f} metros"
        )

        self.execute_next_waypoint(
            res.waypoints,
            0
        )

    # -------------------------------------------------
    # NAVIGATION EXECUTION
    # -------------------------------------------------
    def execute_next_waypoint(
        self,
        waypoints,
        index
    ):

        # -----------------------------
        # ROUTE FINISHED
        # -----------------------------
        if index >= len(waypoints):

            total_duration = (
                self.get_clock().now()
                - self.navigation_start_time
            ).nanoseconds / 1e9

            self.log_and_save(
                "Ruta completada"
            )

            self.log_and_save(
                f"Tiempo total navegación: "
                f"{total_duration:.2f} segundos"
            )

            self.log_and_save(
                f"Distancia total estimada: "
                f"{self.total_distance:.2f} metros"
            )

            self.busy = False
            return

        wp = waypoints[index]

        self.log_and_save(
            f"Yendo a: "
            f"{wp.name} "
            f"({wp.x}, {wp.y})"
        )

        # -----------------------------
        # START TIMER
        # -----------------------------
        self.waypoint_start_time = (
            self.get_clock().now()
        )

        # -----------------------------
        # DIRECT DISTANCE
        # -----------------------------
        dx = (
            self.current_pose.position.x
            - wp.x
        )

        dy = (
            self.current_pose.position.y
            - wp.y
        )

        self.current_waypoint_distance = (
            math.sqrt(dx * dx + dy * dy)
        )

        self.log_and_save(
            f"Distancia directa "
            f"al waypoint: "
            f"{self.current_waypoint_distance:.2f} metros"
        )

        # -----------------------------
        # CREATE GOAL
        # -----------------------------
        goal = PoseStamped()

        goal.header.frame_id = "map"

        goal.header.stamp = (
            self.get_clock().now().to_msg()
        )

        goal.pose.position.x = wp.x
        goal.pose.position.y = wp.y
        goal.pose.position.z = wp.z

        goal.pose.orientation.w = 1.0

        # -----------------------------
        # SEND GOAL
        # -----------------------------
        self.goal_pub.publish(goal)

        self.waiting_after_arrival = False

        if self.wait_timer:
            self.wait_timer.cancel()

        self.wait_timer = self.create_timer(
            0.2,
            lambda: self.check_arrival(
                wp,
                waypoints,
                index
            )
        )

    # -------------------------------------------------
    # ARRIVAL CHECK
    # -------------------------------------------------
    def check_arrival(
        self,
        wp,
        waypoints,
        index
    ):

        if (
            self.current_pose is None
            or self.waiting_after_arrival
        ):
            return

        dx = (
            self.current_pose.position.x
            - wp.x
        )

        dy = (
            self.current_pose.position.y
            - wp.y
        )

        dist = math.sqrt(dx * dx + dy * dy)

        if dist < self.goal_tolerance:

            waypoint_duration = (
                self.get_clock().now()
                - self.waypoint_start_time
            ).nanoseconds / 1e9

            self.log_and_save(
                f"Llegado a {wp.name} | "
                f"Tiempo: {waypoint_duration:.2f} s | "
                f"Distancia directa: {dist:.2f} m"
            )

            self.log_and_save(
                "Esperando 2s..."
            )

            self.waiting_after_arrival = True

            if self.wait_timer:
                self.wait_timer.cancel()

            self.post_arrival_timer = (
                self.create_timer(
                    2.0,
                    lambda: self.after_pause(
                        waypoints,
                        index
                    )
                )
            )

    # -------------------------------------------------
    # PAUSE
    # -------------------------------------------------
    def after_pause(
        self,
        waypoints,
        index
    ):

        if self.post_arrival_timer:

            self.post_arrival_timer.cancel()

            self.post_arrival_timer = None

        self.waiting_after_arrival = False

        self.execute_next_waypoint(
            waypoints,
            index + 1
        )


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