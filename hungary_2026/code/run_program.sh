#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/ubuntu/ydlidar_ws/devel/setup.bash
cd /home/ubuntu
source code/.venv/bin/activate
"$@"
