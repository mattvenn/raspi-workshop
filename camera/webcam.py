#!/usr/bin/python

import os

def capture_image():
    #this can do banners and timestamps
    output = 'frame.jpg'
    command = "fswebcam  --no-banner -r 800x600 -d /dev/video0 %s" % output
    #command = "fswebcam --set brightness=50%% --no-banner -r 800x600 -d /dev/video0 %s" % output
    os.system(command)	


if __name__=="__main__":  
    capture_image()
