#!/usr/bin/python

import os

def capture_image():
    time=25 # 1/20s
    shootmode=1 #time priority
    command = """gphoto2 --set-config /main/capturesettings/shootingmode=%d \
--set-config /main/capturesettings/shutterspeed=%d \
--set-config /main/capturesettings/focusingpoint=0 \
--set-config /main/capturesettings/afdistance=0 \
--capture-image-and-download \
--quiet \
    """ % (shootmode,time)

    status = os.system(command)  
    return status

if __name__=="__main__":  
    capture_image()
