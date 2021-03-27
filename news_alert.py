from sys import excepthook
import tweepy
from multiprocessing.pool import ThreadPool

import requests
import sys
import json


CONSUMER_KEY = "oEj1YVDAR5JkUqzy8lV2qgENw"
CONSUMER_SECRET  = "h24rQes4yIotJ8AftUW7agIvvcswBfL4FHwJGMMUaIabfOa2ic"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALgXOAEAAAAATvx6fzu7VO3WaGQFB17fPl%2BGYSQ%3DXgfsZHcoD5gBe8Ir19TsBsJiLAmm9vbko7jsMERB4aLsBKSykr"

ACCESS_TOKEN = "1125419842389954560-OE0KCfrDi6weg5fMQg18VKoy2K5j8p"
ACCESS_SECRET = "LE8HgxwanwmgeKxw7lN6c8YFYmnGZKsR3py60qLdCyTNb"

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK....")
except:
    print("Error during Authentication")
    sys.exit(1)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['python'])
print("the end")
