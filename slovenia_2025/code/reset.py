import RPi.GPIO as GPIO
from .control.motor import set_speed
from .control.servo import unsafe_steer, stop

set_speed(0)
unsafe_steer(0)
stop()


GPIO.cleanup()