from ..control import servo
from ..sensors import gyroscope

PITCH_SENSITIVITY = 20

def get_pitch_difference():
    
    pitch = gyroscope.get_safe_pitch()
    
    if pitch is None: return None

    return gyroscope.angle_difference(pitch, gyroscope.INITIAL_DIRECTION.value)

def keep_direction(isNegative = False):
    
    pitch_difference = get_pitch_difference()
    if pitch_difference is None:
        return None

    normalized_steer = min(max(-1, pitch_difference / PITCH_SENSITIVITY), 1)

    if isNegative:
        normalized_steer = -normalized_steer

    servo.safe_steer(-normalized_steer)

    return pitch_difference