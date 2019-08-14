import picamera

import picamera.array

 

import numpy as np

import cv2

import time

 

camera = picamera.PiCamera()

camera.resolution = (640,480)

camera.framerate = 15

rawCapture = picamera.array.PiRGBArray(camera, size = (640,480))

 

time.sleep(1)

 

for frame in camera.capture_continuous(rawCapture, format= "bgr",use_video_port=True):

	image = frame.array

	

	cv2.imshow("frame",image)

	key = cv2.waitKey(1)&0xFF

	

	rawCapture.truncate(0)

	

	if key == ord('q'):

		break

		

cv2.destroyAllWindows()
