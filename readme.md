# Innovative Hand Tracking and Finger Counting for Robot Navigation in ROS

🤖🖐️ Exciting Robotics Project Alert!

👁️‍🗨️ Imagine a world where you can control a robot's movements simply by showing it your hand and using your fingers as commands. In this project, I've harnessed the power of computer vision and ROS to make this a reality.

🔍 Hand Tracking: My system employs computer vision algorithms to track the movement and position of your hand in real-time. It can precisely identify the location of each finger, allowing for precise and intuitive control.

🖐️ Finger Counting: With the ability to count fingers, the robot understands your commands effortlessly. Each finger gesture corresponds to a specific action, enabling a wide range of interactions with the robot.

🏁 Robot Navigation: But here's the kicker! Once your hand gesture is detected and translated into a command, our robot uses the Move Base node in ROS to navigate to a predefined point based on your input. It's a game-changer for human-robot interaction.

## Requirements

- ROS Noetic
- Python 3.8
- OpenCV
- MediaPipe
- actionlib
- move_base
## Installation

1. **Install ROS Noetic** following the instructions from the official [ROS installation guide](http://wiki.ros.org/noetic/Installation).

2. **Install dependencies**:
    ```bash
    sudo apt-get install ros-noetic-move-base ros-noetic-actionlib
    pip3 install opencv-python mediapipe
    ```

3. **Clone this repository**:
    ```bash
    git clone https://github.com/sherif1152/ros_finger_count_navigation.git
    ```

## Usage

### Finger Count Publisher Node

This node uses the webcam input to count the number of fingers shown and publishes the count to the `finger_count` topic.

### Run the Finger Count Publisher Node

- ```bash
    rosrun your_package_name finger_count_publisher.py
    ```

- ```bash
    rosrun your_package_name finger_count_publisher.py
    ```
