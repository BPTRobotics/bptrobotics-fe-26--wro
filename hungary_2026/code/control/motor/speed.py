from . import utils

__speed : float = 0

def set_speed(speed : float) -> None:
    global __speed

    if speed > 1 or speed < 0:
        raise ValueError("Speed can only be between 0.0 and 1.0")
    
    __speed = speed
    
    utils.set_speed(__speed * 100)

def get_speed() -> float:
    global __speed
    return __speed