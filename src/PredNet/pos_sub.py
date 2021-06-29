#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32MultiArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     
def pos_listener():
    rospy.init_node('pos_listener', anonymous=True)

    rospy.Subscriber("/pred_pos_topic", Float32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    pos_listener()

