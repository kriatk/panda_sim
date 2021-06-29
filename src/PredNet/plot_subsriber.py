#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
import torch
import numpy as np
from std_msgs.msg import String
from std_msgs.msg    import Float32MultiArray, MultiArrayLayout, MultiArrayDimension
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from find_object import find_object
from geometry_msgs.msg import Point
from specs import localize_target

i = 0
class plot_subscriber:

    def __init__(self):

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/plot_topic",Image,self.callback)



    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)

        global i
        i+=1
        filename = 'image{0}.png'.format(i)
        cv2.imwrite(filename, cv_image)

     

def main(args):

    ps = plot_subscriber()
    rospy.init_node('plot_subscriber', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
