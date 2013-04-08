#!/usr/bin/python
"""
author: matt venn
"""

from datetime import datetime
import os
import tweepy
from tweepy import OAuthHandler

consumer_key= "fF86BdSdopE9FAES5UNgPw"
consumer_secret= "n7G4K80kYQ6NDMQiYn3GY5Hyk82fF2So17Nl1UQdGWE"

access_token= "1336977176-4CgpPJnJBx7kCRqnwLcRbXI3nLpHj44sp3r2bXy"
access_token_secret= "5rLNvZm3JZdkx0K1Jx9jgsqMG6MmGLAQmPdJ7ChtzA"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print "my twitter name:",  api.me().name
hostname = os.uname()[1]
time = datetime.now()

api.update_status("the time on %s is %s" % ( hostname, time ))
