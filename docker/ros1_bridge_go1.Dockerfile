FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    git \
    gnupg2 \
    lsb-release \
    locales \
    netcat \
    iputils-ping \
    && locale-gen en_US en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
    -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros/ubuntu focal main" \
    > /etc/apt/sources.list.d/ros1.list \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu focal main" \
    > /etc/apt/sources.list.d/ros2.list

RUN apt-get update && apt-get install -y \
    ros-noetic-ros-base \
    ros-noetic-joint-state-publisher \
    ros-noetic-robot-state-publisher \
    ros-noetic-xacro \
    ros-foxy-ros-base \
    ros-foxy-robot-state-publisher \
    ros-foxy-ros1-bridge \
    ros-foxy-rmw-cyclonedds-cpp \
    ros-foxy-rmw-fastrtps-cpp \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/unitreerobotics/unitree_ros.git /tmp/unitree_ros \
    && mkdir -p /opt/unitree_go1_ws/src \
    && cp -r /tmp/unitree_ros/robots/go1_description /opt/unitree_go1_ws/src/go1_description \
    && source /opt/ros/noetic/setup.bash \
    && cd /opt/unitree_go1_ws \
    && catkin_make \
    && rm -rf /tmp/unitree_ros

COPY bridge_entrypoint.sh /usr/local/bin/bridge_entrypoint.sh
# COPY ros1_start_go1_description.sh /usr/local/bin/ros1_start_go1_description.sh
# COPY ros2_start_go1_description.sh /usr/local/bin/ros2_start_go1_description.sh
COPY ros2_initialpose_to_udp.py /usr/local/bin/ros2_initialpose_to_udp.py
COPY udp_to_ros1_set_pose.py /usr/local/bin/udp_to_ros1_set_pose.py
COPY fastdds_udp_only.xml /usr/local/share/fastdds_udp_only.xml
COPY ros1_bridge_topics.yaml /usr/local/share/ros1_bridge_topics.yaml

RUN chmod +x /usr/local/bin/bridge_entrypoint.sh \
    # /usr/local/bin/ros1_start_go1_description.sh \
    # /usr/local/bin/ros2_start_go1_description.sh \
    /usr/local/bin/ros2_initialpose_to_udp.py \
    /usr/local/bin/udp_to_ros1_set_pose.py

CMD ["/usr/local/bin/bridge_entrypoint.sh"]
