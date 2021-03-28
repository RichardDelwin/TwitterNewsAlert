import tweepy
from multiprocessing.pool import ThreadPool
import sys
import os 
import src.StreamListener
import json

CONSUMER_KEY = r"fPt4a7istHIo0kh8iS3PhWHK6"
CONSUMER_SECRET  = r"vu7nAlCm3ByaXTln766Ob8O3FMFtF8wzwanugwdRqFkjSRUMF7"
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAALgXOAEAAAAAmKlAQ3YvSv03QvA5pPI90GgOwoo%3D6SpUWP9bMI3xpS3rmGmeSUr7PX926p9uphObSdi40EHphSvLgG"
ACCESS_TOKEN = r"1125419842389954560-wbf9LThY910s44iKbXk0n7aLudJhOJ"
ACCESS_SECRET = r"8CK1YrJE4knhS027Tx83zxoHdmyQNuxYnmUOa7WsGXZ6J"


def initialize(filename=None):

    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(DIR_PATH)

    if not filename:

        keyFile = os.path.join(DIR_PATH, "keys.json")

        if os.path.isfile(keyFile):
            filename = keyFile
        else:
            raise Exception("Specify the keys file")

    with open(filename) as file:
        data = json.load(file)

    global CONSUMER_KEY 
    CONSUMER_KEY = data["CONSUMER_KEY"]
    global CONSUMER_SECRET  
    CONSUMER_SECRET= data["CONSUMER_SECRET"]
    global BEARER_TOKEN 
    BEARER_TOKEN= data["BEARER_TOKEN"]
    global ACCESS_TOKEN 
    ACCESS_TOKEN = data["ACCESS_TOKEN"]
    global ACCESS_SECRET 
    ACCESS_SECRET = data["ACCESS_SECRET"]
    

# auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# api = tweepy.API(auth)

sys.exit(1)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

try:

    api = tweepy.API(auth)

except Exception as e:

    print("Authentication Error")
    print(type(e))
    print(e)

# res = api.verify_credentials()    -----------> Doesn't work!


myStreamListener = StreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['World'])
print("the end")
