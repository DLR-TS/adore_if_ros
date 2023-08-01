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
# *      Thomas Lobig
# ********************************************************************************

import rospy
import time

from std_msgs.msg import Bool


pub = None

def callback_sample(msg):
    print(msg.data)


emergency_stop=False

def get_brake_pedal_state():
    current_state = False
    with open('/var/log/rsyslog/telemetry.log', 'r') as f:
        last_line = f.readlines()[-1]
        current_state = bool(int(last_line.split("brake_pedal_state:")[1].strip()))
    return current_state

if __name__ == '__main__':
    pub = rospy.Publisher('/vehicle0/FUN/HaltAutomation', Bool, queue_size=1)
    rospy.init_node('ecu_emergency_stop_node')
    # run loop:
    r = rospy.Rate(10) # 10hz
    
    print("ECU Emergency stop node starting...", flush = True)
    current_state=False
    last_state=False
    while True:
        if rospy.is_shutdown():
            continue
        current_state = get_brake_pedal_state()
        if current_state != last_state:
            print(f"  brake pedal state: {current_state}", flush = True)
            pub.publish(current_state)
        r.sleep()
        last_state = current_state
    #    time.sleep(.1)
    #    with open('/var/log/rsyslog/telemetry.log', 'r') as f:
    #        last_line = f.readlines()[-1]
    #        current_state = bool(int(last_line.split("brake_pedal_state:")[1].strip()))
    #    print("emergency_stop: {current_state}")
        #while not rospy.is_shutdown():
        #    with open('/var/log/rsyslog/telemetry.log', 'r') as f:
        #        last_line = f.readlines()[-1]
        #        current_state = bool(int(last_line.split("brake_pedal_state:")[1].strip()))
        #    print(f"Publishing emergency_stop: {current_state}")
        #    signal_publish()
        #    pub.publish(current_state)
        #    r.sleep()
        #    last_state=current_state



    # alternatively use ros.spin() to wait until shutdown, if you don't need a run loop
