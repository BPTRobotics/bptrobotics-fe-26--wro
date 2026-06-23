"""LiDAR-based heading estimation for corridor driving (replaces the IMU).

In WRO Future Engineers the robot runs between two parallel walls, so we can
recover the robot's heading *relative to the corridor* from the scan. For each
side wall we collect every valid beam in a window around the perpendicular,
turn them into (x, y) points in the robot frame, and least-squares fit a line.
The line's slope is the heading error: 0 deg = parallel to the wall (driving
straight). Fitting a whole window (instead of two single rays) is robust to the
X4's frequent dropped returns.

Angle convention (same as the rest of the code):
    180 = front, 90 = left, 270 = right, 0/360 = back.
Robot frame: forward = +x, left = +y, so  phi = 180 - lidar_angle.
"""
from math import degrees, radians, cos, sin, atan
from . import utils

# --- tunables ---------------------------------------------------------------
LEFT_CENTER, RIGHT_CENTER = 90, 270   # perpendicular to each side wall
HALF_WINDOW = 45      # deg sampled each side of the wall centre
STEP        = 2       # deg between sampled beams
MIN_POINTS  = 5       # need at least this many hits to trust a wall

# If the robot steers the WRONG way on a straight (hugs / drives into a wall),
# flip this to -1.0.  It inverts the sign of the whole heading signal.
SIGN = 1.0
# ---------------------------------------------------------------------------


def _point(angle_deg, msg):
    """(x, y) of the beam at angle_deg in the robot frame, or None if no echo."""
    d = utils.extract_distance(angle_deg, msg)
    if d is None:
        return None
    phi = radians(180 - angle_deg)
    return d * cos(phi), d * sin(phi)


def _wall_points(msg, center):
    """All valid (x, y) points in the window around one wall centre."""
    pts = []
    a = center - HALF_WINDOW
    while a <= center + HALF_WINDOW:
        p = _point(a, msg)
        if p is not None:
            pts.append(p)
        a += STEP
    return pts


def _wall_heading(msg, center):
    """Least-squares slope of one wall, as a heading angle (deg), or None."""
    pts = _wall_points(msg, center)
    n = len(pts)
    if n < MIN_POINTS:
        return None
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    if sxx < 1e-4:          # points too clustered to define a direction
        return None
    return degrees(atan(sxy / sxx))


def heading_error(msg):
    """Robot heading relative to the corridor, in degrees (0 = parallel).

    Averages both side walls; falls back to whichever wall is visible.
    Returns None if neither wall gives enough points.
    """
    if msg is None:
        return None
    errs = [e for e in (_wall_heading(msg, LEFT_CENTER),
                        _wall_heading(msg, RIGHT_CENTER))
            if e is not None]
    if not errs:
        return None
    return SIGN * (sum(errs) / len(errs))
