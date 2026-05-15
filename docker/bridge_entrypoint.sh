#!/usr/bin/env bash
set -euo pipefail

BRIDGE_CONFIG=/usr/local/share/ros1_bridge_topics.yaml

echo "Checking ROS1 master at ${ROS_MASTER_URI:-<unset>}..."
if ! bash -lc 'set -euo pipefail; set +u; source /opt/ros/noetic/setup.bash; if [[ -f /opt/unitree_go1_ws/devel/setup.bash ]]; then source /opt/unitree_go1_ws/devel/setup.bash; fi; set -u; rostopic list | awk "NR <= 10 { print }"'; then
  echo "Failed to query ROS1 master before starting the bridge."
  echo "Check ROS_MASTER_URI, ROS_IP, and network reachability to the NX."
  exit 1
fi

if ! bash -lc 'set -euo pipefail; set +u; source /opt/ros/noetic/setup.bash; if [[ -f /opt/unitree_go1_ws/devel/setup.bash ]]; then source /opt/unitree_go1_ws/devel/setup.bash; fi; set -u; rosparam load /usr/local/share/ros1_bridge_topics.yaml'; then
  echo "Failed to load ros1_bridge topic config into the ROS1 parameter server."
  exit 1
fi

bash -lc 'set -euo pipefail; exec /usr/local/bin/ros1_start_go1_description.sh' 

bash -lc 'set -euo pipefail; exec /usr/local/bin/ros2_start_go1_description.sh' &
ROS2_DESCRIPTION_PID=$!

bash -lc 'set -euo pipefail; set +u; source /opt/ros/noetic/setup.bash; if [[ -f /opt/unitree_go1_ws/devel/setup.bash ]]; then source /opt/unitree_go1_ws/devel/setup.bash; fi; set -u; exec python3 /usr/local/bin/udp_to_ros1_set_pose.py' &
ROS1_ADAPTER_PID=$!

bash -lc 'set -euo pipefail; set +u; source /opt/ros/foxy/setup.bash; set -u; exec python3 /usr/local/bin/ros2_initialpose_to_udp.py' &
ROS2_ADAPTER_PID=$!
BRIDGE_PID=""

cleanup() {
  kill "${ROS2_DESCRIPTION_PID}" >/dev/null 2>&1 || true
  kill "${ROS1_ADAPTER_PID}" >/dev/null 2>&1 || true
  kill "${ROS2_ADAPTER_PID}" >/dev/null 2>&1 || true
  if [[ -n "${BRIDGE_PID}" ]]; then
    kill "${BRIDGE_PID}" >/dev/null 2>&1 || true
  fi
}

trap cleanup EXIT INT TERM

echo "Loaded ros1_bridge topic config from ${BRIDGE_CONFIG}"
echo "Starting ros1_bridge parameter_bridge with selected topics..."
echo "  Go1 robot description is loaded in ROS1 and consumed natively by ROS2 robot_state_publisher"
echo "  Go1 robot_state_publisher runs natively in ROS2 so RViz2 can consume /tf_static correctly"
echo "  /initialpose is handled by the UDP relay because its ROS2 type differs from ROS1 /slamware_ros_sdk_server_node/set_pose"
echo "  /parameter_events is not bridged because it is a ROS2-native topic with no ROS1 peer"

bash -lc '
  set -euo pipefail

  PARAMETER_BRIDGE_BIN=/opt/ros/foxy/lib/ros1_bridge/parameter_bridge
  ROS1_LIB_DIR=/opt/ros/noetic/lib

  if [[ ! -x "${PARAMETER_BRIDGE_BIN}" ]]; then
    echo "parameter_bridge binary not found at ${PARAMETER_BRIDGE_BIN}"
    exit 127
  fi
  if [[ ! -d "${ROS1_LIB_DIR}" ]]; then
    echo "ROS1 library directory not found at ${ROS1_LIB_DIR}"
    exit 127
  fi

  set +u
  source /opt/ros/noetic/setup.bash
  if [[ -f /opt/unitree_go1_ws/devel/setup.bash ]]; then
    source /opt/unitree_go1_ws/devel/setup.bash
  fi
  unset ROS_DISTRO
  source /opt/ros/foxy/setup.bash
  set -u

  export LD_LIBRARY_PATH="${ROS1_LIB_DIR}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"

  exec "${PARAMETER_BRIDGE_BIN}"
' &
BRIDGE_PID=$!

set +e
wait "${BRIDGE_PID}"
BRIDGE_STATUS=$?
set -e

echo "ros1_bridge parameter_bridge exited with status ${BRIDGE_STATUS}"
exit "${BRIDGE_STATUS}"
