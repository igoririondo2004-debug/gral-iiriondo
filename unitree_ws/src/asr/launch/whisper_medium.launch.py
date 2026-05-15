from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='asr',
            executable='whisper_medium_node',
            name='whisper_medium_node',
            output='screen',
            parameters=[
                {'language': 'es'},
                {'sample_rate': 16000}
            ]
        )
    ])