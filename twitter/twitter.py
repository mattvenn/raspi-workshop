"""
author: matt venn
"""

from datetime import datetime
import os

#the twitter library
import tweepy
from tweepy import OAuthHandler

#here are all the secret keys. If people know these they can pretend they are you
consumer_key= "fF86BdSdopE9FAES5UNgPw"
consumer_secret= "n7G4K80kYQ6NDMQiYn3GY5Hyk82fF2So17Nl1UQdGWE"

access_token= "1336977176-4CgpPJnJBx7kCRqnwLcRbXI3nLpHj44sp3r2bXy"
access_token_secret= "5rLNvZm3JZdkx0K1Jx9jgsqMG6MmGLAQmPdJ7ChtzA"

#create the auth and access tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#get the api
api = tweepy.API(auth)
print "my twitter name:",  api.me().name

#get the bits of information we want to tweet
hostname = os.uname()[1]
time = datetime.now()

#make the post
api.update_status("the time on %s is %s" % ( hostname, time ))
