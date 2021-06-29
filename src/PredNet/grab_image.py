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
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from find_object import find_object
from geometry_msgs.msg import Point
from specs import localize_target
 
class image_converter:
 
    def __init__(self):
        self.obj_pub = rospy.Publisher("/obj_pos",Point)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera1/image_raw",Image,self.callback)

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        try:
            targ, msg = find_object(cv_image)
            print(msg)
            self.obj_pub.publish(msg)
        except CvBridgeError as e:
            print(e)

        if not np.isnan(targ[0]):
            cv2.circle(cv_image, (targ[1],targ[0]), radius=2, color=(0,0,255), thickness=-1)
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)

     

def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
