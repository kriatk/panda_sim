from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from specs import localize_target
from cv_bridge    import CvBridge
import torch
import rospy
import numpy as np

#@nrp.MapRobotSubscriber('camera',         Topic('/camera/image_raw',     Image))
#@nrp.MapRobotPublisher( 'obj_pos_topic', Topic('/obj_pos', Point))
#@nrp.Robot2Neuron()

image_sub = rospy.Subscriber("/camera1/image_raw",Image)
location_pub = rospy.Publisher("/obj_pos",Point)

def find_object(cam_img):

    max_pix_value  = 1.0
    normalizer     = 255.0/max_pix_value
    cam_img = torch.tensor(cam_img).permute(2,1,0)

    targ = localize_target(cam_img)
#    if targ[1] < 100: # otherwise it is detecting something else.
#        targ = (-1, -1)

    msg = Point()
    msg.x = targ[0]
    msg.y = targ[1]

    return targ, msg

