from .. import gyroscope
from .utils import angle_difference
import time

def calibrate():
    attempt = 100

    pitch = gyroscope.get_safe_pitch()
    latest_pitch = -999
    while attempt > 0:
        pitch = gyroscope.get_safe_pitch()
        difference = angle_difference(pitch,latest_pitch)
        if difference < 1 and pitch != latest_pitch:
            break
        attempt -= 1
        latest_pitch = pitch
        time.sleep(.05)