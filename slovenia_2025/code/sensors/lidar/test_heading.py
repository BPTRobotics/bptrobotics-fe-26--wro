"""Live read-out of the LiDAR heading + how many wall points the fit used.

Run (from the repo root):  python3 -m code.sensors.lidar.test_heading

Place the robot between two walls. Columns:
  F/L/R    : raw distance (m) at front/left/right ('inf' = no echo)
  Lpts/Rpts: how many valid beams the left/right wall fit found (need >=5)
  heading  : estimated heading error (deg), ~0 when parallel to the walls
Uses only LiDAR/ROS (no motors). Ctrl-C stops.
"""
from . import setup
from .heading import heading_error, _wall_points, LEFT_CENTER, RIGHT_CENTER
from .utils import extract_distance
from time import sleep

_msg = None


def _cb(m):
    global _msg
    _msg = m


setup.init(_cb)

import rospy


def d(angle):
    v = extract_distance(angle, _msg)
    return " inf " if v is None else f"{v:5.2f}"


print("F(180) L(90) R(270) | Lpts Rpts | heading")
try:
    while not rospy.is_shutdown():
        if _msg is not None:
            lp = len(_wall_points(_msg, LEFT_CENTER))
            rp = len(_wall_points(_msg, RIGHT_CENTER))
            h = heading_error(_msg)
            hs = "none" if h is None else f"{h:6.1f}"
            print(f"F{d(180)} L{d(90)} R{d(270)} | {lp:4d} {rp:4d} | {hs}")
        sleep(0.3)
except KeyboardInterrupt:
    print("\nStopped.")
