#!/usr/bin/env python3

import rospy
import math
from sensor_msgs.msg import LaserScan

# global variable to store the latest lidar scan
msg = None

def lidar_callback(scan_msg):
    """Callback to store latest lidar data."""
    global msg
    msg = scan_msg

def extract_distance(angle_deg: int, msg) -> float:
    """Extracts distance at the specified angle in degrees."""
    idx = int((angle_deg % 360) / (msg.angle_increment * (180 / math.pi)))
    if 0 <= idx < len(msg.ranges):
        val = msg.ranges[idx]
        if val and not math.isinf(val) and val > 0.01:
            return val
    return None

def display_lidar(msg, resolution=5, scale=10):
    """
    Displays a simple radar-like representation of lidar data.
    :param resolution: degrees per step
    :param scale: multiplier for visual scaling
    """
    grid_size = 21
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    center = grid_size // 2
    grid[center][center] = 'R'  # robot position

    for angle in range(0, 360, resolution):
        dist = extract_distance(angle, msg)
        if dist is None:
            continue
        display_dist = min(int(dist * scale), center)
        rad = math.radians(angle)
        x = center + int(display_dist * math.cos(rad))
        y = center + int(display_dist * math.sin(rad))
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = '*'

    # print grid
    print("\n" + "=" * grid_size)
    for row in reversed(grid):
        print(''.join(row))
    print("=" * grid_size)

def main():
    rospy.init_node('lidar_radar_display', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, lidar_callback)  # update topic if yours is different

    rate = rospy.Rate(5)  # 5 Hz update

    print("Waiting for first lidar scan...")
    while not msg and not rospy.is_shutdown():
        rate.sleep()

    print("Starting radar display...")
    try:
        while not rospy.is_shutdown():
            if msg:
                display_lidar(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        print("Exiting...")

if __name__ == '__main__':
    main()
