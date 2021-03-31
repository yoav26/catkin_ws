# Agripper
## ROS package for Cartesian robotic arm using stepper motors 

To run the control node there are two options:
1. roslaunch
2. run the desired node manualy
 
anyway the 'serial_v3_teensy.ino' should be uploaded to the teensy boad.

1. roslaunch
 in terminal run the commend:
 ruslaunch start.launch
 it will launch 4 nodes:
  - serial node (the teensy board as a node)
  - read_location - publish the current position in steps unit
  - move_node - get user input (x,y,z) and execute after pressing Enter
  - home - execute homing
 
2. rosrun
 - each node can be run seperatly with 'rosrun'
 - rosrun [package_name] [node_name]
 - for example:
 - rosrun agripper read_location.py

### ROS kinetic, ubuntu 14.04, Python 2.7.12
