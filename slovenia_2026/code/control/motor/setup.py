import RPi.GPIO as GPIO
from ...configuration import get_config


try:
    pins = get_config()['motor']['pins']
    IN1 = pins['IN1']
    IN2 = pins['IN2']
    ENA = pins['ENA']
except KeyError as e:
    raise KeyError("""
          Configuration error:
          motor.pins.IN1/IN2/ENA doesn't exists
          """)

GPIO.setup(pins['IN1'], GPIO.OUT)
GPIO.setup(pins['IN2'], GPIO.OUT)
GPIO.setup(pins['ENA'], GPIO.OUT)

pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)