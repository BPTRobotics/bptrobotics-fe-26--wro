import yaml
from pathlib import Path

parent_directory : Path = Path(__file__).resolve().parent.parent

config_path : Path = parent_directory / "config.yaml"

with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

print(f"Config loaded succesfully!")

def get_config() -> any:
    return config

import RPi.GPIO as GPIO
try:
    gpiomode = config['pin_settings']['mode']
except KeyError:
    print("GPIO Pin mode wasn't specified")

if gpiomode == 'BOARD':
    GPIO.setmode(GPIO.BOARD)
else:
    GPIO.setmode(GPIO.BCM)
