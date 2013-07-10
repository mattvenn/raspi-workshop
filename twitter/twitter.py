from twython import Twython
import os
from datetime import datetime

#this demo posts tweets from piworkshop (https://twitter.com/piworkshop)

#authenticate, check the README.md for how to set up your own account
twitter = Twython(
    #consumer key
    "fF86BdSdopE9FAES5UNgPw",
    #consumer secret
    "n7G4K80kYQ6NDMQiYn3GY5Hyk82fF2So17Nl1UQdGWE",
    #access_token
    "1336977176-4CgpPJnJBx7kCRqnwLcRbXI3nLpHj44sp3r2bXy",
    #access_token_secret
    "5rLNvZm3JZdkx0K1Jx9jgsqMG6MmGLAQmPdJ7ChtzA",
)

#post a new tweet, use the hostname and time to make it unique
hostname = os.uname()[1]
time = datetime.now()
message = "the time on %s is %s" % ( hostname, time )
print "sending a text tweet..."
twitter.update_status(status=message)
print "sent"

#send a picture tweet
print "sending a tweet with an image..."
photo = open('twitter.png', 'rb')
twitter.update_status_with_media(media=photo, status=message + " with picture")
print "sent"

#get our timeline and print latest 5 out
print "timeline:"
timeline = twitter.get_user_timeline()
for tweet in timeline[0:5]:
    #just show the text
    print "-> " + tweet["text"]

