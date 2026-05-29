import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

import math
import time
import json
import os
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


class HexagonBenchmark(Node):

    def __init__(self):
        super().__init__('hexagon_benchmark')

        # =========================
        # CONFIG
        # =========================
        self.hex_size = 1.25
        self.goal_tol = 0.25
        self.speed_tol = 0.05
        self.num_loops = 1

        # =========================
        # OUTPUT
        # =========================
        base_dir = "/home/tknika/gral-iiriondo/unitree_ws/src/slam_analysis/results"
        self.run_dir = os.path.join(
            base_dir,
            datetime.now().strftime("%Y%m%d_%H%M%S")
        )
        os.makedirs(self.run_dir, exist_ok=True)

        # =========================
        # NAV
        # =========================
        self.goal_pub = self.create_publisher(
            PoseStamped,
            '/move_base_simple/goal',
            10
        )

        # =========================
        # STATE
        # =========================
        self.odom = []

        self.goal_idx = 0
        self.loop_idx = 0

        self.start_time = None
        self.loop_start_time = None
        self.corner_start_time = None

        self.corner_times = []
        self.corner_errors = []

        self.origin = None

        # =========================
        # SUBSCRIPTION
        # =========================
        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(0.2, self.step)

    # =========================================================
    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        vx = msg.twist.twist.linear.x
        vy = msg.twist.twist.linear.y

        speed = math.hypot(vx, vy)

        self.odom.append((time.time(), x, y, speed))

    # =========================================================
    def send_goal(self, x, y):

        msg = PoseStamped()
        msg.header.frame_id = "map"
        msg.header.stamp = self.get_clock().now().to_msg()

        msg.pose.position.x = float(x)
        msg.pose.position.y = float(y)
        msg.pose.orientation.w = 1.0

        self.goal_pub.publish(msg)

    # =========================================================
    # HEXAGON (6 CORNERS)
    # =========================================================
    def build_hexagon(self, x, y):

        r = self.hex_size / 2

        return [
            (x, y),                 # bottom-right

            (x + r, y - r),         # mid-right
            (x + 2*r, y),           # top-right

            (x + 2*r, y + r),       # top-left
            (x + r, y + 2*r),       # mid-left
            (x, y + r),             # bottom-left

            (x, y)                  # close loop
        ]

    # =========================================================
    def closest_point(self, px, py, x1, y1, x2, y2):

        vx = x2 - x1
        vy = y2 - y1

        wx = px - x1
        wy = py - y1

        c1 = vx * wx + vy * wy

        if c1 <= 0:
            return x1, y1

        c2 = vx * vx + vy * vy

        if c2 <= c1:
            return x2, y2

        b = c1 / c2

        return (x1 + b * vx, y1 + b * vy)

    # =========================================================
    def step(self):

        if len(self.odom) == 0:
            return

        _, x, y, speed = self.odom[-1]

        # INIT
        if self.start_time is None:

            self.start_time = time.time()
            self.loop_start_time = time.time()
            self.corner_start_time = time.time()

            self.origin = (x, y)

            self.hexagon = self.build_hexagon(x, y)

            self.send_goal(*self.hexagon[0])

            return

        tx, ty = self.hexagon[self.goal_idx]

        dist = math.hypot(x - tx, y - ty)

        # ARRIVAL
        if dist < self.goal_tol and speed < self.speed_tol:

            corner_time = time.time() - self.corner_start_time

            self.corner_times.append(corner_time)
            self.corner_errors.append(dist)

            self.get_logger().info(
                f"Corner {self.goal_idx} reached | "
                f"error {dist:.3f} | "
                f"time {corner_time:.2f}s"
            )

            self.goal_idx += 1
            self.corner_start_time = time.time()

            # LOOP COMPLETE
            if self.goal_idx >= len(self.hexagon):

                loop_time = time.time() - self.loop_start_time

                self.get_logger().info(
                    f"Loop {self.loop_idx} finished in {loop_time:.2f}s"
                )

                self.loop_idx += 1
                self.goal_idx = 0
                self.loop_start_time = time.time()

                if self.loop_idx >= self.num_loops:

                    self.finish()
                    rclpy.shutdown()
                    return

                self.send_goal(*self.hexagon[0])

            else:

                self.send_goal(*self.hexagon[self.goal_idx])

    # =========================================================
    def compute_tracking_error(self):

        errors = []

        for _, x, y, _ in self.odom:

            best = float("inf")

            for i in range(len(self.hexagon)):

                x1, y1 = self.hexagon[i]
                x2, y2 = self.hexagon[(i + 1) % len(self.hexagon)]

                cx, cy = self.closest_point(x, y, x1, y1, x2, y2)

                d = math.hypot(x - cx, y - cy)

                best = min(best, d)

            errors.append(best)

        return {
            "mean": sum(errors) / len(errors) if errors else 0.0,
            "max": max(errors) if errors else 0.0
        }

    # =========================================================
    def compute_smoothness(self):

        angles = []

        for i in range(2, len(self.odom)):

            _, x0, y0, _ = self.odom[i - 2]
            _, x1, y1, _ = self.odom[i - 1]
            _, x2, y2, _ = self.odom[i]

            v1 = (x1 - x0, y1 - y0)
            v2 = (x2 - x1, y2 - y1)

            n1 = math.hypot(*v1)
            n2 = math.hypot(*v2)

            if n1 > 0 and n2 > 0:

                dot = v1[0] * v2[0] + v1[1] * v2[1]

                cos_a = max(-1, min(1, dot / (n1 * n2)))

                angles.append(math.acos(cos_a))

        return sum(angles) / len(angles) if angles else 0.0

    # =========================================================
    def finish(self):

        total_time = time.time() - self.start_time

        start_x, start_y = self.origin
        end_x, end_y = self.odom[-1][1], self.odom[-1][2]

        final_drift = math.hypot(end_x - start_x, end_y - start_y)

        report = {
            "total_time": total_time,
            "tracking_error_mean": self.compute_tracking_error()["mean"],
            "tracking_error_max": self.compute_tracking_error()["max"],
            "smoothness": self.compute_smoothness(),
            "final_drift": final_drift,
            "corner_times": self.corner_times,
            "corner_errors": self.corner_errors
        }

        with open(os.path.join(self.run_dir, "report.json"), "w") as f:
            json.dump(report, f, indent=4)

        # ROBOT TRAJECTORY
        sx = [-p[2] for p in self.odom]
        sy = [p[1] for p in self.odom]

        # HEXAGON REFERENCE
        hx = [-p[1] for p in self.hexagon]
        hy = [p[0] for p in self.hexagon]

        plt.figure(figsize=(8, 8))

        plt.plot(sx, sy, label="Robot (/odom)")
        plt.plot(hx, hy, "--", label="Hexagon")

        plt.axis("equal")
        plt.grid()
        plt.legend()

        plt.title("Hexagon Benchmark")

        plt.savefig(
            os.path.join(self.run_dir, "trajectory.png"),
            dpi=200
        )

        plt.close()


def main():
    rclpy.init()
    node = HexagonBenchmark()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()