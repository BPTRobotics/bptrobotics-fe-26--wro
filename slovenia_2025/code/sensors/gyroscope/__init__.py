from .setup import sensor, INITIAL_DIRECTION
from . import utils                  
from .utils import *        
from ._reset import reset, safe_reset
from ._calibrate import calibrate

from threading import Thread

def get_pitch():
    try:
        return utils.get_pitch(sensor)
    except (KeyError, ValueError) as e:
        print(f"Key / Value error: {e}")

isResetting = False

def safe_reset_thread():
    global isResetting
    isResetting = True
    safe_reset()
    isResetting = False

def get_safe_pitch():
    if isResetting:
        return None
    
    pitch = get_pitch()
    if pitch is None:
        Thread(target=safe_reset(),daemon=True).start()
    return pitch