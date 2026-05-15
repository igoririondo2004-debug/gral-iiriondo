#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 3 || $# -gt 4 ]]; then
  echo "Uso: $0 <x> <y> <yaw_rad> [frame_id]"
  echo "Ejemplo: $0 1.0 0.5 1.57 map"
  exit 1
fi

X="$1"
Y="$2"
YAW="$3"
FRAME_ID="${4:-map}"

set +u
source /opt/ros/humble/setup.bash
set -u

export ROS_DOMAIN_ID="${ROS_DOMAIN_ID:-42}"
export ROS_LOCALHOST_ONLY="${ROS_LOCALHOST_ONLY:-0}"
export RMW_IMPLEMENTATION="${RMW_IMPLEMENTATION:-rmw_cyclonedds_cpp}"

read -r QZ QW < <(
  python3 - "$YAW" <<'PY'
import math
import sys
yaw = float(sys.argv[1])
print(f"{math.sin(yaw / 2.0)} {math.cos(yaw / 2.0)}")
PY
)

echo "Publishing goal to /move_base_simple/goal"
echo "  frame_id=${FRAME_ID}"
echo "  x=${X}"
echo "  y=${Y}"
echo "  yaw_rad=${YAW}"

exec ros2 topic pub -r 2 --times 3 /move_base_simple/goal geometry_msgs/msg/PoseStamped "{
  header: {stamp: now, frame_id: '${FRAME_ID}'},
  pose: {
    position: {x: ${X}, y: ${Y}, z: 0.0},
    orientation: {x: 0.0, y: 0.0, z: ${QZ}, w: ${QW}}
  }
}"
