from ...configuration import get_config

MIN, MAX, OFFSET = None, None, None
try:
    config = get_config()
    CHANNEL = config['servo']['CHANNEL']

    constraits = config['servo'].get('direction_constraits', None)
    if constraits:
        MIN = constraits.get('min', None)
        if MIN is None:
            print("servo.direction_constraits wasn't given")
            MIN = 180
        MAX = constraits.get('max', None)
        if MAX is None:
            print("servo.min wasn't given")
            MAX = 180
        OFFSET = constraits.get('offset', None)
        if OFFSET is None:
            print("servo.max wasn't given")
            OFFSET = 0
    else:
        print("No servo.constraits were given")
except KeyError:
    raise KeyError("""
          Configuration error:
          servo.CHANNEL is not availible
          """)
    

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)


