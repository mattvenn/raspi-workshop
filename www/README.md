# a web server

Running a web server on the pi is a way of remote controlling it from another computer. In this example, we start the web server running on port 8080, so you'd need to point your browser to

    http://x.x.x.x:8080/

Where x.x.x.x is your pi's IP address. A simple index.html file is served, and if you click a link we can run a file to flash an led connected to pin 8.

Start the server like this:

    sudo python serve.py

# Connections

add an LED and a resistor in series to pin 8 of the header. There is an example circuit on the workshop resources.
