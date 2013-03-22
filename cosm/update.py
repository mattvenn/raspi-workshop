#!/usr/bin/python
from PachubeFeedUpdate import *

#private key stored in a file
keyfile="api.key"
key=open(keyfile).readlines()[0].strip()

#feed id
feed_id = "120508"
pfu = PachubeFeedUpdate(feed_id,key)

# do some stuff; gather data, repeating as necessary for any number of datastreams
f=open("/proc/uptime","r");
uptime_string=f.readline()
uptime=uptime_string.split()[0]
pfu.addDatapoint('uptime', uptime)

# finish up and submit the data
pfu.buildUpdate()
pfu.sendUpdate()
