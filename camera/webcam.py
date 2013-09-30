"""
author: matt venn
"""

#import the library to call external commands
import os

#this function takes a photo using the fswebcam command
def capture_image(filename):
    #the fswebcam command can also do banners and timestamps
    command = "fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename
    status = os.system(command)
    return status


#take a photo
capture_image('picture.jpg')
