from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Argumentos
    user_debug = LaunchConfiguration('user_debug')

    declare_user_debug = DeclareLaunchArgument(
        'user_debug',
        default_value='false'
    )

    # Ruta al xacro
    robot_description_content = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare('go1_description'),
            'xacro',
            'robot.xacro'
        ]),
        ' DEBUG:=', user_debug
    ])

    robot_description = {
        'robot_description': robot_description_content
    }

    # Nodos

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{
            'use_gui': True
        }]
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[
            robot_description,
            {'publish_frequency': 1000.0}
        ]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        output='screen',
        arguments=[
            '-d',
            PathJoinSubstitution([
                FindPackageShare('go1_description'),
                'launch',
                'check_joint.rviz'
            ])
        ]
    )

    return LaunchDescription([
        declare_user_debug,
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ])
