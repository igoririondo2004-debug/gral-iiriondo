from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    robot_ip_arg = DeclareLaunchArgument(
        'robot_ip',
        default_value='192.168.123.161',
        description='Unitree robot IP address for the high-level UDP SDK interface.',
    )

    standing_mode_node = Node(
        package='standing_mode',
        executable='standing_mode',
        name='standing_mode',
        output='screen',
        parameters=[{
            'robot_ip': LaunchConfiguration('robot_ip'),
        }],
    )

    return LaunchDescription([
        robot_ip_arg,
        standing_mode_node,
    ])
