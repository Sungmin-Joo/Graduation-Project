import picamera

import picamera.array

 

import numpy as np

import cv2

import time

while(1):

	with picamera.PiCamera() as camera:

		with picamera.array.PiRGBArray(camera) as output:

			camera.resolution = (680,480)

			camera.capture(output,'bgr')

			image = output.array

			cv2.imshow("frame", image)

			key = cv2.waitKey(1)&0xFF

			output.truncate(0)

	if key == ord('q'):

		break

cv2.destroyAllWindows()	
