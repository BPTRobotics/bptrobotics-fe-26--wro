from ..sensors import lidar
from ctypes import c_float
import time

msg = None
def callback(__msg):
    global msg
    msg = __msg

LOG = True
LOG_FILE = "/home/ubuntu/log.txt"

if LOG:
    from atexit import register as areg
    file = open(LOG_FILE,"w").close()
    file = open(LOG_FILE,"a")
    areg(file.close)
def printall(msg):
    if not LOG: return

    for degree in range(360):
        distance = lidar.utils.extract_distance(degree, msg)
        if distance is None:
            distance = float('inf')
        file.write(f"{distance}\n")

lidar.setup.init(callback)

import time

try:
    sd = lidar.utils.extract_distance(180, msg) if msg else None
    while not msg or sd is None or sd == 0:
        if msg:
            sd = lidar.utils.extract_distance(180, msg)
        print("Waiting for LIDAR to initialize...")
        time.sleep(0.5)  # standard sleep
except KeyboardInterrupt:
    print("\nStopped by user")

printall(msg)
print("START DISTANCE:", sd)
START_DISTANCE = c_float(sd)
