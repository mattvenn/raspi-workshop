Interrupts provide a way of listening to a button (or other input) connected to a pin. Instead of checking every second (called polling) to see if the pin is changed, we can attach an interrupt. Then our code is interrupted when something happens.

Connect a button between pins 7 and 9 (gpio4 and ground).

The python script connects gpio4 pullup resistor, and an interrupt is called if gpio4 goes low
