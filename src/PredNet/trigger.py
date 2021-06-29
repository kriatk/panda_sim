#!/usr/bin/env python
import sys
import rospy
import numpy as np
from std_msgs.msg import String, Float32MultiArray, UInt8




class trigger:

    def __init__(self):
        self.sub = rospy.Subscriber("/pred_pos_topic", Float32MultiArray, self.callback)
        self.pub = rospy.Publisher('/trig', UInt8, queue_size=1)
        self.trig = 0

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.data = np.asarray(data.data, dtype=np.float64)
        self.trig_handler()
    
    def trig_handler(self):
        if self.data[16]>0.5 and self.data[16]<0.6:
            self.trig = 1
        else:
            self.trig = 0
        print(self.trig)
        self.pub.publish(self.trig)

        

def main(args):
    rospy.init_node('trigger', anonymous=True)
    trig_obj = trigger()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")


if __name__ == '__main__':
    main(sys.argv)
