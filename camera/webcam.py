"""
author: matt venn
"""

#import the library to call external commands
import os

filename = 'picture.jpg'
#os.system() runs a linux command called fswebcam which takes a photo
os.system("fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename)
print("taken photo!")

