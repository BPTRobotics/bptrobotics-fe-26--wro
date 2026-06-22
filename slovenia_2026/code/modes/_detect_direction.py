from ctypes import c_int

DIRECTION = c_int(-1) # -1 for left, 1 for right

from . import lidar_manager
from ..sensors.lidar.utils import extract_distance
from time import sleep

DETECTION_THRESHOLD = 1.5

def detect_direction():
    global DIRECTION
    while True:
        if lidar_manager.msg:
            distance = extract_distance(90, lidar_manager.msg)
            if distance != None and distance != 0:
                if distance < DETECTION_THRESHOLD:
                    DIRECTION.value = 1
                else:
                    DIRECTION.value = -1
                break
            else:
                print(f"No valid distance ({distance})")
        else:
            print("No valid lidar data")
        sleep(0.5)
    print(f"Distance: {distance}")