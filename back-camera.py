#!/usr/bin/python

#Import the required dependencies
import picamera
from PIL import Image
from time import sleep

#Start a loop with the Pi camera
with picamera.PiCamera() as camera:
	#Set the resolution, fps, and then start the preview
    camera.resolution = (1024, 600)
    camera.framerate = 24
    camera.start_preview()
    camera.rotation = 180

    #The image size MUST match the camera resolution (1024 x 600)
	#otherwise the code will not work
    img = Image.open('camera-overlay.png')
    

    # Add the image as a camera overlay
    img_overlay = camera.add_overlay(img.tobytes(), size=img.size)
	#Make the overlay semi-transparent, and change the
	#default layer from 0 (under the camera layer) to 3 (over the camera layer)
    img_overlay.alpha = 128
    img_overlay.layer = 3

    # Wait till the user terminates the script
    while True:
        sleep(1)
