#!/bin/bash

hostname=raspberrypi4
echo $hostname > /etc/hostname
sed -e "s/raspberrypi$/$hostname/" /etc/hosts > /tmp/hosts
mv /tmp/hosts /etc/hosts

apt-get update
apt-get -y install ipython
apt-get -y install git

#our repo - doesn't seem to work still
mkdir /home/pi/.ssh
echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> /home/pi/.ssh/config
git clone git@github.com:/mattvenn/raspi-workshop.git

#for remote login with hostname
apt-get -y install avahi-daemon libnss-mdns

#for easy python package install
apt-get -y install python-pip

#modules for i2c and heartbeat
echo i2c-bcm2708  >> /etc/modules
echo i2c-dev >> /etc/modules
echo ledtrig_heartbeat >> /etc/modules

#remove module blacklist
cat /dev/null > /etc/modprobe.d/raspi-blacklist.conf

#enable led heartbeat - needs fixing as it replaces in more than one place
sed -e 's/exit 0/echo heartbeat >\/sys\/class\/leds\/led0\/trigger/' /etc/rc.local > /tmp/rc.local
echo 'exit 0' >> /tmp/rc.local
mv /tmp/rc.local /etc/rc.local
chmod a+x /etc/rc.local

#libs for i2c
apt-get -y install python-smbus
apt-get -y install i2c-tools

#for rpio
apt-get -y install python-dev

#python libs for our workshop demos
pip install RPIO
pip install mechanize
pip install pyserial

#other programs
apt-get install -y fswebcam
