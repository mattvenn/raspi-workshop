#!/usr/bin/python
"""
author: matt venn
"""

#import the library to call external commands
import os

#this function takes a photo using the fswebcam command
def capture_image():
    #this can do banners and timestamps
    output = 'frame.jpg'
    command = "fswebcam  --no-banner -r 800x600 -d /dev/video0 %s" % output
    #command = "fswebcam --set brightness=50%% --no-banner -r 800x600 -d /dev/video0 %s" % output
    status = os.system(command)	
    return status


#if this script is run from the command line...
if __name__=="__main__":  
    capture_image()
