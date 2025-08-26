from .utils import get_primary_color, get_area
import time

while True:
    primary_color = get_primary_color(NOISE_THREASHOLD=100)
    if primary_color:
        area = get_area(primary_color)
        print("Noise size:", area)
    else:
        print("No noise detected")
    time.sleep(.5)