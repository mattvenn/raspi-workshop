# Servos

servos provide an easy way to create movement. They need an external power supply - the raspberry pi isn't powerful enough.

# connections

* attach a servo to pin 8 of the pi.
* connect the usb power lead from the powered hub to the + and - rails on the breadboard.
* connect a capacitor across the + and - rails of the breadboard
* connect the ground of the raspberry pi (pin 6) to the - rail on the breadboard.

# Other information

using the PWM library: http://pythonhosted.org/RPIO/pwm_py.html
