from .. import gyroscope
from time import sleep as time_sleep

if __name__ == '__main__':
    while True:
        time_sleep(0.01)
        pitch = gyroscope.get_safe_pitch()
        if not pitch:
            print("Error, no pitch")
            continue
        print(f"Pitch: {pitch:.2f}")