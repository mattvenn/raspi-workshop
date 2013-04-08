import tweepy
from tweepy import OAuthHandler

consumer_key= "khwzzasbbUHHxWwEn05uhw"
consumer_secret= "7vOGEBYR7CYFoZFI4CYtLD506uLKNhzXMOPVeoLSRs"

access_token= "19602951-MvhiSbEA56DzBLGlOOnYKjDHknijzYjYzZgZPsD1p"
access_token_secret= "wk4EkPHwG2AFHzlvNpoJlxONNyPsOWocEM0olSGwwo"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print "name",  api.me().name

api.update_status("Tweepy")
