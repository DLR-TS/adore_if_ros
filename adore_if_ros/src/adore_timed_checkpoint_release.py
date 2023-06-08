#!/usr/bin/env python3
# ********************************************************************************
# * Copyright (C) 2017-2020 German Aerospace Center (DLR).
# * Eclipse ADORe, Automated Driving Open Research https://eclipse.org/adore
# *
# * This program and the accompanying materials are made available under the
# * terms of the Eclipse Public License 2.0 which is available at
# * http://www.eclipse.org/legal/epl-2.0.
# *
# * SPDX-License-Identifier: EPL-2.0
# *
# * Contributors:
# *   Thomas Lobig
# ********************************************************************************

# this node will send a checkpoint clearance signal (boolean true) by the next full minute
# ctrl-c to abo
import sys
import time
import datetime
import calendar
try:
    import rospy
    from std_msgs.msg import Bool
except:
    print("rospy not found, need to source ROS to run this")
    sys.exit(-1)

import adore_if_ros_msg.msg


class Clearing:
    def __init__(self):
        vehicle_clearance_topic = "/VEH/Checkpoints/clearance"
        self.pub = rospy.Publisher(vehicle_clearance_topic, Bool, queue_size=10)

    def on_timer_elapsed(self,event):
        self.pub.publish(Bool(True))
        print("cleared at " + str(rospy.get_time()))


if __name__ == '__main__':
    rospy.init_node('adore_timed_checkpoint_release', anonymous=True)

    now = rospy.get_time()
    print("Epoch time is: " + str(now))
    next_minute_in_ns = float(int(now) - int(now) % 60 + 60)
    print("starting in " + str(next_minute_in_ns  - now) + " seconds")

    c = Clearing()
    timer = rospy.Timer(rospy.Duration(next_minute_in_ns - rospy.get_time()),c.on_timer_elapsed,oneshot=True)

    rospy.spin()
    