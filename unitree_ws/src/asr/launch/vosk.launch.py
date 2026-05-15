from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='asr',
            executable='vosk_node',
            name='asr_node',
            output='screen',
            parameters=[
                {'language': 'es'},
                {'sample_rate': 16000}
            ]
        )
    ])