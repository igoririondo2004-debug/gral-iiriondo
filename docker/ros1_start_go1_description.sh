#!/usr/bin/env bash
set -euo pipefail

set +u
source /opt/ros/noetic/setup.bash
if [[ -f /opt/unitree_go1_ws/devel/setup.bash ]]; then
  source /opt/unitree_go1_ws/devel/setup.bash
fi
set -u

GO1_PACKAGE_PATH="$(rospack find go1_description)"
GO1_MODEL_FILE="$(find "${GO1_PACKAGE_PATH}" -type f \( -path '*/urdf/*.xacro' -o -path '*/urdf/*.urdf' \) | sort | head -n 1)"

if [[ -z "${GO1_MODEL_FILE}" ]]; then
  echo "Could not find a Go1 URDF/xacro under ${GO1_PACKAGE_PATH}"
  exit 1
fi

echo "Using Go1 model file: ${GO1_MODEL_FILE}"

if [[ "${GO1_MODEL_FILE}" == *.xacro ]]; then
  ROBOT_DESCRIPTION_CONTENT="$(xacro "${GO1_MODEL_FILE}")"
else
  ROBOT_DESCRIPTION_CONTENT="$(cat "${GO1_MODEL_FILE}")"
fi

GO1_FILE_URI_BASE="file://${GO1_PACKAGE_PATH}/"
ROBOT_DESCRIPTION_CONTENT="${ROBOT_DESCRIPTION_CONTENT//package:\/\/go1_description\//${GO1_FILE_URI_BASE}}"

rosparam set /robot_description "${ROBOT_DESCRIPTION_CONTENT}"
printf '%s' "${ROBOT_DESCRIPTION_CONTENT}" > /tmp/go1_robot_description.urdf
