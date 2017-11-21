#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from basics.msg import Complex
def callback(msg):
    print('Real:', msg.real)
    print('Imaginary:', msg.imaginary)
    print('')

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin()