# Reading temperature

Many temperature sensors have an analogue voltage to represent temperature. The pi doesn't have an analogue to digital converter (ADC) so we need to use a digital sensor.

Here we're reading temperature with the ds18b20 temperature sensor. This is a one wire device, which means we can send and receive information down just one wire. They can be chained in a long row to get multiple temperature readings.

# Connections

See the image here: http://webshed.org/wiki/File:Fritzing_rPI_DS1820.png

* Connect a 4k7 resistor between pins 2 and 3 of the sensor
* connect 3.3v (raspi pin 1) to pin 3 of the sensor
* connect ground (raspi pin 6) to pin 1 of the sensor
* connect pin 7 of the raspi to pin 2 of the sensor

# More information

The ds18b20 is made by maxim. The datasheet is here: http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf
