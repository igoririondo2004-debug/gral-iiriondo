#!/usr/bin/env bash
set -euo pipefail

[[ -f /tmp/go1_robot_description.urdf ]] || {
  echo "/tmp/go1_robot_description.urdf not found"
  exit 1
}

python3 - <<'PY'
from pathlib import Path

robot_description = Path('/tmp/go1_robot_description.urdf').read_text()
indented = ''.join(f'      {line}\n' for line in robot_description.splitlines())
content = (
    '/robot_state_publisher:\n'
    '  ros__parameters:\n'
    '    robot_description: |\n'
    f'{indented}'
)
Path('/tmp/go1_robot_state_publisher.yaml').write_text(content)
PY

set +u
source /opt/ros/foxy/setup.bash
set -u

exec ros2 run robot_state_publisher robot_state_publisher --ros-args --params-file /tmp/go1_robot_state_publisher.yaml
