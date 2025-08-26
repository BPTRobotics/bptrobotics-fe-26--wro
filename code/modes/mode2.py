from .direction_manager import keep_direction
from ..sensors import gyroscope
from ..control import motor
from time import sleep
from . import _detect_direction
from ..Button import wait_for_button_press

def start():
    gyroscope.INITIAL_DIRECTION.value += 90 *  _detect_direction.DIRECTION.value
    pitch_difference = 999

    motor.set_speed(.75)
    motor.backward()
    while abs(pitch_difference or 10) > 10:
        wait_for_button_press()
        pitch_difference = keep_direction()
        if pitch_difference is not None:
            motor.backward()
            print(f"MODE (2): Pitch difference: {pitch_difference:.2f}")
        else:
            motor.stop()
    motor.stop()