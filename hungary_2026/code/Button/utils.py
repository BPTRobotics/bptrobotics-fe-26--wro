import RPi.GPIO as GPIO
from .setup import button_pin
import time
from ..control import motor
from .. import LCD

def wait_for_button_press():
    if GPIO.input(button_pin) == GPIO.LOW:
        return
    motor.stop()
    LCD.set_mode(4)
    print(f"Waiting for button press... ({GPIO.input(button_pin)})")
    while GPIO.input(button_pin) == GPIO.HIGH:
        time.sleep(1)
    print("Button pressed!")
    LCD.set_mode(0)