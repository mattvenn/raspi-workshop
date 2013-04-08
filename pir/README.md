# detecting a person's movement

We're using a PIR (passive infra red sensor) from oomlout: http://www.oomlout.co.uk/motion-detector-pir-p-276.html
When people move, the sensor's output pin goes high.

# Connections

* connect the PIR's ground pin to the pi's ground pin (6)
* connect the PIR's + pin to the pi's 3.3v pin (1)
* connect the PIR's output pin to pin 7 on the pi
