#!/usr/bin/env python
import sys
import rospy
import numpy as np
from std_msgs.msg import String, UInt8

def callback(data):
    print(data.data)
     
def trig_listener():
    rospy.init_node('trig_listener', anonymous=True)

    rospy.Subscriber("/trig", UInt8, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    trig_listener()
