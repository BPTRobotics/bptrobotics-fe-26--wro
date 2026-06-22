from .utils import set_angle
from .setup import MIN, MAX, OFFSET

__angle : float = 0

def steer(direction) -> None:
    global __angle
    if direction > 1 or direction < -1:
        raise ValueError(f"Direction can only be between -1.0 and 1.0. [{direction}]")
    
    __angle = direction
    
    unmapped_direction = 90 * (direction + 1)

    constraited_direction = min(MAX, max(MIN, unmapped_direction + OFFSET))

    set_angle( constraited_direction )

    return constraited_direction
    
def safe_steer(direction):
    global __angle
    if round(direction,2) != round(__angle,2):
        return steer(direction)
    return None

def get_direction() -> float:
    return __angle