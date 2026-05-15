#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-go1-ros1-bridge}"
NX_IP="${NX_IP:-192.168.123.15}"
NX_HOSTNAME="${NX_HOSTNAME:-nx}"
RASPBERRY_IP="${RASPBERRY_IP:-192.168.12.1}"
ROS_MASTER_URI="${ROS_MASTER_URI:-http://${NX_IP}:11311}"
ROS_DOMAIN_ID_VALUE="${ROS_DOMAIN_ID:-42}"
BRIDGE_RMW_IMPLEMENTATION_VALUE="${BRIDGE_RMW_IMPLEMENTATION:-rmw_fastrtps_cpp}"
FASTRTPS_PROFILE_HOST_PATH="$(dirname "$0")/fastdds_udp_only.xml"
FASTRTPS_PROFILE_CONTAINER_PATH="/usr/local/share/fastdds_udp_only.xml"

ROUTE_TO_RASPBERRY="$(ip route get "${RASPBERRY_IP}")"
HOST_ROS_IP="${HOST_ROS_IP:-$(awk '{for (i = 1; i <= NF; ++i) if ($i == "src") {print $(i + 1); exit}}' <<< "${ROUTE_TO_RASPBERRY}")}"
HOST_NET_IFACE="${HOST_NET_IFACE:-$(awk '{for (i = 1; i <= NF; ++i) if ($i == "dev") {print $(i + 1); exit}}' <<< "${ROUTE_TO_RASPBERRY}")}"
CYCLONEDDS_URI_VALUE="${CYCLONEDDS_URI:-<CycloneDDS><Domain><General><NetworkInterfaceAddress>${HOST_NET_IFACE}</NetworkInterfaceAddress></General></Domain></CycloneDDS>}"

DOCKER_BIN=(docker)
docker info >/dev/null 2>&1 || DOCKER_BIN=(sudo -E docker)

[[ -n "${HOST_ROS_IP}" ]] || { echo "Exporta HOST_ROS_IP manualmente."; exit 1; }
[[ -n "${HOST_NET_IFACE}" ]] || { echo "Exporta HOST_NET_IFACE manualmente."; exit 1; }

[[ "${ROS_DOMAIN_ID_VALUE}" =~ ^[0-9]+$ ]] && (( ROS_DOMAIN_ID_VALUE >= 0 && ROS_DOMAIN_ID_VALUE <= 232 )) || {
    echo "ROS_DOMAIN_ID inválido"; exit 1
}

echo "Building image ${IMAGE_NAME}..."
"${DOCKER_BIN[@]}" build \
  -t "${IMAGE_NAME}" \
  -f "$(dirname "$0")/ros1_bridge_go1.Dockerfile" \
  "$(dirname "$0")"

DOCKER_ADD_HOST=()
if [[ -n "${NX_IP}" && -n "${NX_HOSTNAME}" ]]; then
    DOCKER_ADD_HOST=(--add-host "${NX_HOSTNAME}:${NX_IP}")
fi

DOCKER_RMW_EXTRA_ENV=()
if [[ "${BRIDGE_RMW_IMPLEMENTATION_VALUE}" == "rmw_cyclonedds_cpp" ]]; then
    DOCKER_RMW_EXTRA_ENV=(-e CYCLONEDDS_URI="${CYCLONEDDS_URI_VALUE}")
fi

echo "Launching bridge and opening a shell inside the container..."
echo "  ROS_MASTER_URI=${ROS_MASTER_URI}"
echo "  ROS_IP=${HOST_ROS_IP}"
echo "  HOST_NET_IFACE=${HOST_NET_IFACE}"
echo "  BRIDGE_RMW_IMPLEMENTATION=${BRIDGE_RMW_IMPLEMENTATION_VALUE}"
if [[ -n "${RMW_IMPLEMENTATION:-}" ]]; then
    echo "  Ignoring host RMW_IMPLEMENTATION=${RMW_IMPLEMENTATION}"
fi

exec "${DOCKER_BIN[@]}" run --rm -it \
  --net=host \
  --ipc=host \
  "${DOCKER_ADD_HOST[@]}" \
  -e DISPLAY="${DISPLAY:-:0}" \
  -e QT_X11_NO_MITSHM=1 \
  -e FASTRTPS_DEFAULT_PROFILES_FILE="${FASTRTPS_PROFILE_CONTAINER_PATH}" \
  -e ROS_MASTER_URI="${ROS_MASTER_URI}" \
  -e ROS_IP="${HOST_ROS_IP}" \
  -e ROS_DOMAIN_ID="${ROS_DOMAIN_ID_VALUE}" \
  -e ROS_LOCALHOST_ONLY=0 \
  -e RMW_IMPLEMENTATION="${BRIDGE_RMW_IMPLEMENTATION_VALUE}" \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v "${FASTRTPS_PROFILE_HOST_PATH}:${FASTRTPS_PROFILE_CONTAINER_PATH}:ro" \
  -v "/home/igor/gral-iiriondo/unitree_ws/src/go1_description/meshes:/opt/unitree_go1_ws/src/go1_description/meshes:ro" \
  "${DOCKER_RMW_EXTRA_ENV[@]}" \
  "${IMAGE_NAME}" \
  bash -lc '/usr/local/bin/bridge_entrypoint.sh & echo "bridge_entrypoint running in background"; exec bash'

# exec "${DOCKER_BIN[@]}" run --rm -it \
#   --net=host \
#   --ipc=host \
#   "${DOCKER_ADD_HOST[@]}" \
#   -e FASTRTPS_DEFAULT_PROFILES_FILE="${FASTRTPS_PROFILE_CONTAINER_PATH}" \
#   -e ROS_MASTER_URI="${ROS_MASTER_URI}" \
#   -e ROS_IP="${HOST_ROS_IP}" \
#   -e ROS_DOMAIN_ID="${ROS_DOMAIN_ID_VALUE}" \
#   -e ROS_LOCALHOST_ONLY=0 \
#   -e RMW_IMPLEMENTATION="${BRIDGE_RMW_IMPLEMENTATION_VALUE}" \
#   -v "${FASTRTPS_PROFILE_HOST_PATH}:${FASTRTPS_PROFILE_CONTAINER_PATH}:ro" \
#   "${DOCKER_RMW_EXTRA_ENV[@]}" \
#   "${IMAGE_NAME}"