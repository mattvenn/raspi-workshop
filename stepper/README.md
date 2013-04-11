# Stepper motors

Stepper motors are powerful and capable of moving a specific number of steps in either direction. This makes them great for making precise robots. However, they aren't as straight forward to drive as an LED. So we'll use a stepper driver board.

The stepper board's wiring details are on the workshop resources. Take care to wire it up correctly as a misconnection could damage the driver board or the pi. If in doubt, ask!

# Important notes!

* When you connect the power, check the temperature of the chip on the driver board. If it gets hot immediately, turn off the power and ask for help.
* The driver chip does heat up after extended use.
* Don't disconnect or connect the motor while power is connected - this will break the driver board.

# Connections

The stepper driver needs 4 connections from the pi:

* step: take a step in the direction specified
* dir: which direction to step in
* sleep: the driver is asleep to save power, we need to turn this pin high to wake it up
* ground: to create the electrical circuit, we need a ground connection

In total, these are the connections needed:

* connect pi pin 7 to the step pin of the driver board
* connect pi pin 11 to the dir pin of the driver board
* connect pi pin 1 (+3.3v) to the sleep pin of the driver board
* connect the ground pin of the driver board to the - rail on the breadboard
* connect the ground of the raspberry pi (pin 6) to the - rail on the breadboard
* connect a wire from the + rail on the breadboard to the stepper psu pin on the driver board
* connect the usb power lead from the powered hub to the + and - rails on the breadboard

# Other information

We're using a driver board detailed here: http://www.pololu.com/catalog/product/2134
