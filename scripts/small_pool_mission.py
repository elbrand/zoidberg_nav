#!/usr/bin/env python
import roslib
roslib.load_manifest('zoidberg_nav')
import rospy
import time

from navigation_client import Command

# setup the command module
rospy.init_node('navigation_client')
co = Command()

try:
    # start the mission
    #rospy.sleep(2.)
    co.begin()
    # mission specifications
    #co.dh_change(.2, 270, 10)
    #co.heading_change(300, 20)
    co.set_rc_velocity(1600, 1500, .2, 270, 10)
except rospy.ROSInterruptException:
    rospy.loginfo("Program interrupted")
finally:
    # make sure communication is terminated cleanly
    co.finished()
