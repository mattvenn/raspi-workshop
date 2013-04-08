This example shows reading data from an I2C device. I2C is like USB for microcontrollers. It's an easy way of adding strings of peripherals to the raspberry pi. The raspberry pi also supports SPI which is similar but requires an extra pin.

thanks to John Neek for the c code:
http://www.john.geek.nz/2013/02/update-bosch-bmp085-source-raspberry-pi/

adafruit example doesn't work from github: 
http://forums.adafruit.com/viewtopic.php?f=19&t=38293&p=189036&hilit=bmp085#p189036
fixed by using an alternative i2c lib:
http://forums.adafruit.com/viewtopic.php?f=8&t=38255&p=190468&hilit=bmp085#p190364
