# Detecting a person's movement

We're using a PIR (passive infra red sensor) from oomlout: http://www.oomlout.co.uk/motion-detector-pir-p-276.html
When people move, the sensor's output pin goes high. The sensor is very sensitive, especially when movement is close by.

# Connections

Gotcha - the wires from the PIR are not the normal colours. Ground is blue, and output is black.

* connect the PIR's ground pin to the pi's ground pin (6)
* connect the PIR's + pin to the pi's 5v pin (2)
* connect the PIR's output pin to pin 8 on the pi
