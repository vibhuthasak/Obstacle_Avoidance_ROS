# Obstacle_Avoidance_ROS
Project in action : [Watch on youtube](https://www.youtube.com/watch?v=wcXuUG4BWAU&t=9s)

## Step by Step ROS Command Explanation

1. First you need to Launch the ROS node.

   ```roslaunch testbot_description testbot_gazebo.launch```

   testbot_description is the package name that I gave. And testbot_gazebo.launch file can be found at /launch folder
   After executing this command, Gazebo will open like below.
   ![alt text](https://github.com/vibhuthasak/Obstacle_Avoidance_ROS/blob/master/1.png)

**Everthing looking great so far right ?** 

2. Now you need to run the python script that is created to listen sensor data from our virtual robot and move the robot.
   
   ```rosrun testbot_description sensor_data_listerner.py```
   

### Python Script Explanation in brief:
   
   The python script is available at Obstacle_Avoidance_ROS/scripts/sensor_data_listener.py path.
   
   The script is simply subcribes to ```/scan``` topic's ```sensor_msgs.msg.LaserScan``` message. The message is modified using    the ```LaserScanProcess()``` function.
   
   ```rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , LaserScanProcess)```
   
   
   And it is publishing commands to ```/cmd_vel``` topic and the message type is Twist.
   
   ```pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)```
   
   If you echo the ```/cmd_vel``` topic using following command
   
   ```rostopic echo cmd_vel```
   
   You will see it is printing __Linear__ and __Angular__ velocities.
   
**DONE**
