Steps:

git clone https://github.com/dadhichis/excercise_2.git
Copy canny_edge_my_face package in your catkin workspace

catkin_make
OR 
catkin_make canny_edge_my_face

source ~/catkin_ws/devel/setup.bash
roscore

source ~/catkin_ws/devel/setup.bash
rosrun usb_cam usb_cam_node
OR
Any other package to access laptop camera via ROS. This will require to change the subscriber topic name in file face_canny_edge_detector.py at line 25 image_topic_name (Default: image_topic_name = '/usb_cam/image_raw').
OR
Follow the installation guide at the end


source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws/canny_edge_my_face/scripts/ 
python face_canny_edge_detector.py

source ~/catkin_ws/devel/setup.bash
rqt_image_view
Select topic /edge_detected_image


Edge parameters:
Adjust edge detection thresholds at line 36 of face_canny_edge_detector.py (Default: 40, 100).


---NOTE: Installation steps---

mkdir -p ~/catkin_ws/src

cd ~/catkin-ws/src

git clone https://github.com/bosch-ros-pkg/usb_cam.gi

cd ..

catkin_make

source ~/catkin-ws/devel/setup.bash

rosrun usb_cam usb_cam_node
