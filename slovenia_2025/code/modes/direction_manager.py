from ..control import servo
from . import lidar_manager
from ..sensors.lidar.heading import heading_error

# Steering gain: heading error (deg) -> steer command. Larger = gentler.
PITCH_SENSITIVITY = 20


def get_pitch_difference():
    """Heading error vs the corridor walls, in degrees (0 = parallel), or None.

    Name kept for compatibility with the mode code that used the gyro.
    """
    return heading_error(lidar_manager.msg)


def keep_direction(isNegative=False):
    pitch_difference = get_pitch_difference()
    if pitch_difference is None:
        return None

    normalized_steer = min(max(-1, pitch_difference / PITCH_SENSITIVITY), 1)
    if isNegative:
        normalized_steer = -normalized_steer

    servo.safe_steer(-normalized_steer)
    return pitch_difference
