from .setup import kit, CHANNEL

def set_angle(angle):   
    kit.servo[CHANNEL].angle = angle

def stop():
    kit._pca.channels[CHANNEL].duty_cycle = 0