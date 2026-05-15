# for the go1 description configuration

1 - ros2 launch go1_description go1_rviz.launch.py

2 - ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link base_visual
