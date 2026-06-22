from ..configuration import get_config

try:
    button_pin = get_config()['BUTTON']['pin']
except KeyError:
    print("BUTTON.PIN is not configured")

import RPi.GPIO as GPIO

GPIO.setup(button_pin, GPIO.IN)