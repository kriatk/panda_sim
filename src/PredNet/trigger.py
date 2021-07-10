#!/usr/bin/env python
import sys
import rospy
import numpy as np
from std_msgs.msg import String, Float32MultiArray, UInt8




class trigger:

    def __init__(self):
        self.sub = rospy.Subscriber("/pred_pos_topic", Float32MultiArray, self.callback)
        self.pub_trig = rospy.Publisher('/trig', UInt8, queue_size=1)
        self.pub_grasp = rospy.Publisher('/grasp', UInt8, queue_size=1)
        self.trig = 0
        self.grasp = 0
        self.count = False
        self.i = 0

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.data = np.asarray(data.data, dtype=np.float64)
        self.trig_handler()
    
    def trig_handler(self):
        if self.data[16]>0.3 and self.data[16]<0.4:
            self.trig = 1
            self.count = True
        else:
            self.trig = 0
            self.grasp = 0
        
        if self.count is True:
            self.i += 1

        if self.i == 4:
            self.grasp = 1
            self.count = False
            self.i = 0
 
        self.pub_trig.publish(self.trig)
        self.pub_grasp.publish(self.grasp)
        print(self.trig)
        print(self.grasp)
            

def main(args):
    rospy.init_node('trigger', anonymous=True)
    trig_obj = trigger()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")


if __name__ == '__main__':
    main(sys.argv)
