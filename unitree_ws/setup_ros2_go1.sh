#!/usr/bin/env bash
set -euo pipefail

#sudo ip route add 192.168.123.0/24 via 192.168.12.1 || true

set +u
source /opt/ros/humble/setup.bash
set -u

export ROS_DOMAIN_ID="${ROS_DOMAIN_ID:-42}"
export ROS_LOCALHOST_ONLY="${ROS_LOCALHOST_ONLY:-0}"
export RMW_IMPLEMENTATION="${RMW_IMPLEMENTATION:-rmw_cyclonedds_cpp}"

echo "ROS2 environment ready:"
echo "  ROS_DOMAIN_ID=${ROS_DOMAIN_ID}"
echo "  ROS_LOCALHOST_ONLY=${ROS_LOCALHOST_ONLY}"
echo "  RMW_IMPLEMENTATION=${RMW_IMPLEMENTATION}"

exec bash
