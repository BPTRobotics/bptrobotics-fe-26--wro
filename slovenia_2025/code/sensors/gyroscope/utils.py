from math import atan2, degrees

def quaternion_to_euler(qw, qx, qy, qz):
    roll = atan2(2.0 * (qw * qx + qy * qz), 1.0 - 2.0 * (qx**2 + qz**2))
    return degrees(roll)

def get_pitch(sensor):
    try:
        qw, qx, qy, qz = sensor.quaternion  
        return quaternion_to_euler(qw, qx, qy, qz)
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"Error occurred while reading quaternion: {e}")

def angle_difference(from_angle: float, to_angle: float) -> float:
    diff = (to_angle - from_angle + 180) % 360 - 180
    return diff if diff != -180 else 180
