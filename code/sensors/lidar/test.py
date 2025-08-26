

from .utils import extract_distance
from .utils import stop_master

def default_callback(msg):
    try:
        """Callback for LIDAR data."""
        
        front = extract_distance(180, msg)
        left = extract_distance(90, msg)
        right = extract_distance(270, msg)

        print(f"Front: {front if front else 'inf'} m")
        print(f"Left: {left if left else 'inf'} m")
        print(f"Right: {right if right else 'inf'} m")
    except Exception as e:
        stop_master()
        raise e
        exit(0)

from . import setup

setup.init(default_callback)

import rospy
rospy.spin()
