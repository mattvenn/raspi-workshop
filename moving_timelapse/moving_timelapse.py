#!/usr/bin/python

#import our libraries
import webcam 
import stepper
import time

camera_delay=1.68

#take a hundred photos
for step in range(400):
    print step

    #take a photo
    webcam.capture_image(str(step)+".jpg")

    #take a step
    stepper.step()

    #time delay, camera takes
    time.sleep(2-camera_delay)

