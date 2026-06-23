from .direction_manager import keep_direction
from ..control import motor
from ..sensors import lidar
from time import sleep
from . import lidar_manager
from ..Button import wait_for_button_press


def start(DISTANCE_=.75):
    motor.set_speed(1)
    distance = 0

    while True:
        wait_for_button_press()
        pitch_diff = keep_direction()
        if pitch_diff is None:
            motor.stop()
        else:
            motor.backward()

        if pitch_diff is not None:
            print(f"MODE (1): Heading error: {pitch_diff:.2f}")

        if lidar_manager.msg:
            distance = lidar.utils.extract_distance(180, lidar_manager.msg)
        else:
            motor.stop()
            continue

        if (distance or DISTANCE_) < DISTANCE_:
            break

        sleep(0.05)
    motor.stop()
