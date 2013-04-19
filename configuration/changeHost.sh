#!/bin/bash
#author: matt venn

if [ "$#" -ne 1 ] ; then
        echo "$0: hostname required"
        exit 1
fi
hostname=$1
echo using $hostname for hostname
echo $hostname > /etc/hostname
sed -e "s/raspberrypi[0-9]\?$/$hostname/" /etc/hosts > /tmp/hosts
mv /tmp/hosts /etc/hosts

echo "now reboot"
