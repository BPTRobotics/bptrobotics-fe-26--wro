import rospy
from sensor_msgs.msg import LaserScan
from . import utils
from atexit import register as areg

process = None

def init(callback):
    global process
    if not utils.test_master():
        process = utils.start_master()

    rospy.init_node('lidar_data_printer', anonymous=True)

    rospy.Subscriber('/scan', LaserScan, callback)

    rospy.loginfo("✅ LIDAR initialized.")

areg(utils.stop_master)