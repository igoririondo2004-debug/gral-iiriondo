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
            executable='speech_to_goal_main_planner_node_logs',
            name='speech_to_goal_main_planner_logs',
            output='screen',
            parameters=[
                {"map_name": "tknika_proba_handia"},
            ]
        ),


        # COMPLEMENTARY NODES
        Node(
            package='mapping_configuration',
            executable='mapping_publishers',
            name='mapping_publishers',
            output='screen'
        ),

        Node(
            package='aruco_detector',
            executable='aruco_mapper_node',
            name='aruco_mapper_node',
            output='screen'
        ),

        Node(
            package='standing_mode',
            executable='standing_mode',
            name='standing_mode',
            output='screen'
        ),

    ])