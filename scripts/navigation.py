#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sensor_msgs.msg
import random
import numpy as np
from geometry_msgs.msg import Twist
from itertools import groupby

LINX = 0.2 #Always forward linear velocity.
THRESHOLD = 1.5 #THRESHOLD value for laser scan.

def LaserScanProcess(data):
    range_vals = np.arange(len(data.ranges))
    ranges = np.array(data.ranges)
    range_mask = np.logical_and((ranges > 0.5) , (ranges < THRESHOLD))
    ranges = list(ranges(range_mask))
    gap_list = []
    for k, g in groupby(enumerate(data), lambda (i,x):i-x):
        gap_list.append(map(itemgetter(1), g))


def main():
    rospy.init_node('listener', anonymous=True)

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , LaserScanProcess)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        command = Twist()
        command.linear.x = LINX
        command.angular.z = angz
        pub.publish(command)
        rospy.spin()
        rate.sleep()

if __name__ == '__main__':
    main()
