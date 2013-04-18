#!/usr/bin/python

#import our libraries, we have links to these files in the current directory
import webcam 
import stepper
import time

#how long our webcam takes to take a photo
camera_delay=1.68

#take a photo every 2 seconds
sleep_time = 2 - camera_delay

#take a lot of photos
num_photos = 400

#take a lot of photos
for step in range(num_photos):
    print step

    #take a photo
    webcam.capture_image(str(step)+".jpg")

    #take a step
    stepper.step()

    #time delay, camera takes
    time.sleep(sleep_time)
