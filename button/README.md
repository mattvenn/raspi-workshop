# Detecting a button press

To detect if a button is pressed we need to make something change when the button is pressed. Either we can have the voltage on the pin be high, and when we press the button it goes low - or the other way round.

To make the voltage on the pin be high, we use a pull up resistor. This is a resistor connected between the pin, and the raspberry pi's 3.3v. Then we can wire the button between the pin and the raspberry pi's 0v (also called ground).

Luckily we can avoid adding a resistor, because we can use the GPIO library to turn on an internal pull up resistor (pull down is also available). Have a look at the code to see how this is done.

# Connections

* Connect a button between pins 8 and 9.
