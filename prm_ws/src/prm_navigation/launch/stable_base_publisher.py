#!/usr/bin/env python

import roslib
roslib.load_manifest('prm_navigation')

import rospy
import tf


if __name__ == '__main__':
    # initialize node
    rospy.init_node('base_stabilizer_tf')
    # print in console that the node is running
    rospy.loginfo('started listener node !')
    # create tf listener
    listener = tf.TransformListener()
    # set the node to run at 100 hz
    rate = rospy.Rate(100.0)
    # initialize broadcaster
    br = tf.TransformBroadcaster()

    # loop forever until roscore or this node is down
    while not rospy.is_shutdown():
        try:
            # listen to transform
            pose = listener.lookupTransform('/odom', '/base_link', rospy.Time(0))
            br.sendTransform((pose[0][0], pose[0][1], pose[0][2]), tf.transformations.quaternion_from_euler(0, 0, tf.transformations.euler_from_quaternion(pose[1])[2]), rospy.Time.now(), "base_stabilized", "odom")
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        # sleep to control the node frequency
        rate.sleep()
