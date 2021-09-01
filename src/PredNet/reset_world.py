import rospy
from subprocess import call
from std_srvs.srv import Empty
import random as rn


def main():

    rospy.wait_for_service('/gazebo/reset_world')
    reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
    reset_world()

#    power = rn.randrange(10,50,10)
#    command = "rosservice call /robot_ns/conveyor/control " +str(power)
#    call(command, shell=True)
#    print(power)    
    

if __name__ == "__main__":
    rospy.init_node('reset_world')
    while not rospy.is_shutdown():
        rospy.sleep(80)
        main()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
