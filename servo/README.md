# Servos

servos provide an easy way to create movement. They need an external power supply - the raspberry pi isn't powerful enough. We'll use the powered hub to provide the power using a special lead.

We set the angle of the servo by pulsing a pin on the raspberry pi. The length of time the pulse is on for sets the angle of the servo. Luckily for us, the RPIO library has some features for controlling servos. Check the code to see how.

# connections

* connect the usb power lead from the powered hub to the + and - rails on the breadboard
* connect the ground of the raspberry pi (pin 6) to the - rail on the breadboard
* connect a wire from the - rail on the breadboard to the black wire of the servo
* connect a wire from the + rail on the breadboard to the red wire on the servo
* connect the servo's white wire to pin 8 of the pi.

# Other information

using the PWM library: http://pythonhosted.org/RPIO/pwm_py.html
