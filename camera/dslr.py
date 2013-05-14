#import the library to call external commands
import os

#this function takes a photo using the gphoto2 command
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

#take a photo
capture_image()
