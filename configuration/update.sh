#adventure game
git clone git@github.com:mattvenn/raspi-adventure.git
./raspi-adventure/setup.sh 

#refresh workshop files
rm -rf raspi-workshop/
git clone git@github.com:mattvenn/raspi-workshop.git

#install vnc
sudo apt-get install tightvncserver
