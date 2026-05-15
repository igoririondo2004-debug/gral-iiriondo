from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='speech_to_goal',
            executable='intent_classifier_node',
            name='intent_classifier_node',
            output='screen'
        ),

        Node(
            package='speech_to_goal',
            executable='speech_to_goal_llm_node',
            name='speech_to_goal_llm_service',
            output='screen'
        ),

        Node(
            package='speech_to_goal',
            executable='speech_to_goal_main_planner_node',
            name='speech_to_goal_main_planner',
            output='screen'
        ),

    ])