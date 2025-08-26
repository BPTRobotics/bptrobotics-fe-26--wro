from . import direction_manager
from ..control import motor, servo
from ..sensors import lidar, camera, gyroscope
from . import lidar_manager
from .. import LCD
from ..Button import wait_for_button_press

from time import sleep


# ------------------------
# SENSOR READING FUNCTIONS
# ------------------------
def get_primary_color():
    """Fetch the primary detected color from the camera."""
    return camera.get_primary_color()


def scan_lidar_area(msg, middle, scan_range, min_distance):
    """Scan lidar data and return a list of 'hot' degrees where an object is detected."""
    hot_degrees = []
    for degree in range(int(middle - scan_range), int(middle + scan_range)):
        distance = lidar.utils.extract_distance(degree, msg)
        if distance and distance < min_distance:
            hot_degrees.append(degree)
    return hot_degrees


# ------------------------
# OBJECT DETECTION LOGIC
# ------------------------
def detect_object_and_angle(msg, pitch_diff, scan_range=20, min_distance=1):
    """Detect object using lidar and return its middle degree if found."""
    middle = 180 + pitch_diff
    hot_degrees = scan_lidar_area(msg, middle, scan_range, min_distance)

    if hot_degrees:
        return sum(hot_degrees) / len(hot_degrees)
    return None

is_too_near = False
pitch_diff = 0
# ------------------------
# DECISION & STEERING
# ------------------------
def decide_and_steer(color_id, middle_degree, steer_by=40):
    global pitch_diff
    global is_too_near
    """Decide action based on color and steer accordingly."""
    if color_id == 1:
        desired_direction = middle_degree - 180 - steer_by
        LCD.set_mode(3)
    elif color_id == 2:
        desired_direction = middle_degree - 180 + steer_by
        LCD.set_mode(2)
    else:
        raise ValueError("Unknown color ID")

    middle_degree_distance = lidar.utils.extract_distance(middle_degree, lidar_manager.msg)
    desired_direction_diff = gyroscope.utils.angle_difference(desired_direction, gyroscope.get_pitch())
    print(f"Desired direction difference: {(desired_direction_diff or 0):.2f}, Desired direction: {(desired_direction or 0):.2f}, Middle degree distance: {(middle_degree_distance or 0):.2f} Middle degree: {(middle_degree or 0):.2f}")
    if middle_degree_distance is not None:
        if middle_degree_distance < 40 and abs(desired_direction_diff) > 50:
            print(f"Too much angle difference, stopping ({middle_degree_distance:.2f})")
            is_too_near = True
            pitch_diff = direction_manager.keep_direction(isNegative=True)
            return desired_direction

    normalized_direction = min(max(-1, desired_direction / direction_manager.PITCH_SENSITIVITY), 1)
    servo.safe_steer(normalized_direction)

    return desired_direction


# ------------------------
# MAIN CONTROL LOOP
# ------------------------
def start(DISTANCE_=1):
    global pitch_diff
    global is_too_near
    motor.set_speed(1)

    pitch_diff = 0

    is_too_near = False

    while True:
        wait_for_button_press()

        if not lidar_manager.msg:
            motor.stop()
            continue

        primary_color = get_primary_color()

        if primary_color != 0:
            middle_degree = detect_object_and_angle(
                lidar_manager.msg, pitch_diff, scan_range=20, min_distance=DISTANCE_
            )

            if middle_degree is not None:
                decide_and_steer(primary_color['ID'], middle_degree)
                pitch_diff = direction_manager.get_pitch_difference()

            lidar_manager.printall(lidar_manager.msg)
        else:
            print(f"MODE (2): Pitch difference: {pitch_diff:.2f}")
            LCD.set_mode(0)

        if not is_too_near:
            motor.backward()

        else:
            is_too_near = False
            motor.forward()

        if primary_color == 0:
            pitch_diff = direction_manager.keep_direction()

        sleep(0.005)

    motor.stop()

