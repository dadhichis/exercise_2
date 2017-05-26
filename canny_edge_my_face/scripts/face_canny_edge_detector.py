#!/usr/bin/env python
"""
Created on Thu May 25 2017

@author: Dadhichi Shukla
"""
# NOTE: Run the following first: 
# rosrun usb_cam usb_cam_node
# OR 
# any other package to run laptop camera with ros
# and accordingly change the topic name at line 25
# image_topic_name = '/usb_cam/image_raw'

import rospy
import cv2 # Canny edge detector, convert to grayscale, etc.
from sensor_msgs.msg import Image # ROS image sensor
from cv_bridge import CvBridge, CvBridgeError # ROS image to Opencv image

class canny_edge_detect_camera:
    def __init__(self):
        self.image_pub = rospy.Publisher('edge_detected_image',Image)
    
        self.bridge = CvBridge()
        # Change image topic if package other than usb_cam is used
        image_topic_name = '/usb_cam/image_raw'
        self.image_sub = rospy.Subscriber(image_topic_name,Image,self.callback)

    def callback(self,rgb_img):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(rgb_img, 'bgr8') # converting ros image message to opencv image
        except CvBridgeError as e:
            print(e)
            
        # RGB to Gray
        cv_image2 = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
        # Canny edge detection
        cv_image2 = cv2.Canny(cv_image2,40,100) # Canny thresholds default: 40, 100
        # Display original image
        cv2.imshow('Camera', cv_image)
        # Display edge detected image
        #cv2.imshow('Canny edge detection', cv_image2)
        cv2.waitKey(3)
        # Or run rqt_image_view in the terminal and select /edge_detected_image topic
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image2)) 
        except CvBridgeError as e:
            print(e)

def main():
    # ros node init
    rospy.init_node('cv_camera')
    # detect edge features
    canny_edge_detect_camera()  
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Exit')
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()