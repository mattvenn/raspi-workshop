#adventure game
git clone git@github.com:mattvenn/raspi-adventure.git
./raspi-adventure/setup.sh 

#refresh workshop files
rm -rf raspi-workshop/
git clone git@github.com:mattvenn/raspi-workshop.git

sudo pip install RPi.GPIO --upgrade

#install vnc
sudo apt-get install tightvncserver

sudo sh -c "echo 'nameserver 8.8.8.8' > /etc/resolv.conf"

sudo sh -c "echo 'iface eth0 inet static
address 192.168.0.15
netmask 255.255.255.0
gateway 192.168.0.1' >> /etc/network/interfaces"
