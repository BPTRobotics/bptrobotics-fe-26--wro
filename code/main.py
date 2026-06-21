from . import LCD
LCD.set_mode(1)

from . import modes
from .control import servo, motor
import RPi.GPIO as GPIO
import rospy
import signal
import sys

def cleanup():
    print("Cleaning up: stopping motors, servos, ROS, GPIO...")
    servo.stop()
    motor.stop()
    if rospy.core.is_initialized():
        rospy.signal_shutdown("Program exiting")
    GPIO.cleanup()
def signal_handler(sig, frame):
    print("Ctrl+C pressed. Exiting gracefully...")
    cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)  

try:
    LCD.set_mode(0)
    modes.open_manager.start()
except Exception:
    import traceback
    traceback.print_exc()
    cleanup()
    sys.exit(1)
cleanup()
