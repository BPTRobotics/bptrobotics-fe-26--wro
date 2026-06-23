"""90-degree turn into the next corridor, using only the LiDAR.

Without the IMU we can't track an absolute 90 deg, so instead we hold a full
steering lock toward the turn direction and drive until the robot has clearly
swung into the new corridor: the front has opened up AND the new side walls
read as roughly parallel. mode1 then refines the heading on the next straight.
"""
from ..control import motor, servo
from ..sensors import lidar
from ..sensors.lidar.heading import heading_error
from time import sleep, time
from . import _detect_direction, lidar_manager
from ..Button import wait_for_button_press

# --- tunables (expect to tune these on the track) --------------------------
TURN_STEER    = 1.0     # steering lock during the turn (0..1)
TURN_SPEED    = 0.75    # motor speed during the turn
FRONT_CLEAR   = 1.2     # m: front counts as "open" past this
ALIGN_TOL     = 12      # deg: |heading error| below this = aligned with new corridor
MIN_TURN_TIME = 0.7     # s: don't allow completion before this (we start aligned)
# ---------------------------------------------------------------------------


def start():
    direction = _detect_direction.DIRECTION.value   # -1 = left, +1 = right

    motor.set_speed(TURN_SPEED)
    servo.safe_steer(TURN_STEER * direction)        # full lock into the turn
    motor.backward()

    t0 = time()
    while True:
        wait_for_button_press()
        msg = lidar_manager.msg
        if not msg:
            motor.stop()
            continue
        motor.backward()

        front = lidar.utils.extract_distance(180, msg)
        err = heading_error(msg)

        turned_enough = (time() - t0) > MIN_TURN_TIME
        front_open = (front is None) or (front > FRONT_CLEAR)
        aligned = (err is not None) and (abs(err) < ALIGN_TOL)

        if turned_enough and front_open and aligned:
            break

        sleep(0.02)

    servo.safe_steer(0)
    motor.stop()
