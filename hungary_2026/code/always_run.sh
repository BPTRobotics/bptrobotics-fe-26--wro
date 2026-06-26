#!/bin/bash

# 1. Source ROS and your workspace (systemd won't do this for you)
source /opt/ros/noetic/setup.bash
source /home/ubuntu/ydlidar_ws/devel/setup.bash

# 2. Force ROS onto loopback — critical for the no-wifi venue
export ROS_MASTER_URI=http://127.0.0.1:11311
export ROS_IP=127.0.0.1

# 3. Wait for the LiDAR to enumerate before launching
#    (USB may not be ready the instant systemd fires)
for i in $(seq 1 30); do
    [ -e /dev/ydlidar ] && break
    sleep 1
done

# 4. Hand off to roslaunch (exec replaces the shell, so systemd
#    tracks roslaunch directly)
exec roslaunch ydlidar_ros_driver X4.launch
