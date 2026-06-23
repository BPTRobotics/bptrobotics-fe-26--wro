import RPi.GPIO as GPIO
from .setup import IN1, IN2, pwm

def forward() -> None:
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def backward() -> None:
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def stop() -> None:
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def set_speed(speed) -> None:
    pwm.ChangeDutyCycle(speed)