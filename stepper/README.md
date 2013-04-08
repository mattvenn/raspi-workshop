# Stepper motors

Stepper motors are powerful and capable of moving a specific number of steps in either direction. This makes them great for making precise robots. However, they aren't as straight forward to drive as an LED. So we'll use a stepper driver board.

The stepper board's wiring details are on the workshop resources. Take care to wire it up correctly as a misconnection could damage the driver board or the pi. If in doubt, ask!

# Important notes!

* When you connect the power, check the temperature of the chip on the driver board. If it gets hot immediately, turn off the power and ask for help.
* The driver chip does heat up after extended use.
* Don't disconnect or connect the motor while power is connected - this will break the driver board.

# Connections

The stepper driver needs 3 connections from the pi:

* step: take a step in the direction specified
* dir: which direction to step in
* pwm: we can control the current in the stepper motor (and hence it's strength) using the pwm control.

In total, these are the connections needed:

* connect pi pin 7 to the step pin of the driver board
* connect pi pin 11 to the dir pin of the driver board
* connect pi pin 8 to the pwm pin of the driver board
* connect the ground pin of the driver board to the - rail on the breadboard
* connect the ground of the raspberry pi (pin 6) to the - rail on the breadboard
* connect a wire from the + rail on the breadboard to the logic psu pin on the driver board
* connect a wire from the + rail on the breadboard to the stepper psu pin on the driver board
* connect the usb power lead from the powered hub to the + and - rails on the breadboard

# Other information

The driver chip we're using is the Allegro 3967: http://www.allegromicro.com/Products/Motor-Driver-And-Interface-ICs/Bipolar-Stepper-Motor-Drivers/A3967.aspx
