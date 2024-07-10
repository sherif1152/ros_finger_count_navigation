#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion
import threading


# Define goal poses for finger counts 1 to 3
goal1 = Pose(Point(-10.321713, 4.864092, 0.0), Quaternion(0.0, 0.0, 0.0, 1.60))
goal2 = Pose(Point(-5.657850, 4.229460, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))
goal3 = Pose(Point(1.629680, -6.754504, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))

# Initialize state variables
current_goal = None
waiting_for_goal = False

# Create an action client for the move_base action server
move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

# Define a callback function to process the received finger count
def finger_count_callback(data):
    global current_goal, waiting_for_goal
    finger_count = data.data
    rospy.loginfo("Received Finger Count: %d", finger_count)

    if finger_count == 1:
        if current_goal is None or not move_base_client.get_state() in [actionlib.GoalStatus.ACTIVE, actionlib.GoalStatus.PENDING]:
            # If there's no current goal or the current goal is not active, set a new goal
            current_goal = goal1
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'map'  # Change 'map' to your desired frame
            goal.target_pose.pose = current_goal
            move_base_client.send_goal(goal)
            waiting_for_goal = True
    elif finger_count == 2:
        if not waiting_for_goal:
            # Handle finger_count 2 here
            current_goal = goal2  # Set the goal to goal2 for finger_count 2
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'map'  # Change 'map' to your desired frame
            goal.target_pose.pose = current_goal
            move_base_client.send_goal(goal)
            waiting_for_goal = True
    elif finger_count == 3:
        if not waiting_for_goal:
            # You can add handling for finger_count 3 here
            current_goal = goal3  # Set the goal to goal2 for finger_count 2
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'map'  # Change 'map' to your desired frame
            goal.target_pose.pose = current_goal
            move_base_client.send_goal(goal)
            waiting_for_goal = True
            pass
    else:
        rospy.logwarn("Finger Count %d is not mapped to a goal.", finger_count)

# Define a function to periodically check if the current goal has been reached
def check_goal_reached():
    global waiting_for_goal
    rate = rospy.Rate(1)  # Adjust the rate as needed
    while not rospy.is_shutdown():
        if waiting_for_goal:
            state = move_base_client.get_state()
            if state == actionlib.GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal Reached")
                waiting_for_goal = False
        rate.sleep()

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('finger_count_subscriber')

    # Create a subscriber for the 'finger_count' topic
    rospy.Subscriber('finger_count', Int32, finger_count_callback)

    # Wait for the action server to start
    move_base_client.wait_for_server()

    # Start the goal-reached checking thread
    goal_reached_thread = threading.Thread(target=check_goal_reached)
    goal_reached_thread.start()

    # Spin to keep the node alive
    rospy.spin()

