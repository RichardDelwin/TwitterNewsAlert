import tweepy
# from multiprocessing.pool import ThreadPool
import sys
import os
import src.StreamListener as StreamListener
from src.StreamSettings import StreamSettings


def authorize():

    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    try:

        api = tweepy.API(auth)

    except Exception as e:

        print("Authentication Error")
        print(type(e))
        print(e)
        sys.exit(1)

    return api


def startNewsALert(filename, json=True, textFile=False):

    api = authorize()
    stream_settings = StreamSettings()
    keywords = None

    if json:
        try:
            status, keywords = stream_settings.get_keywords_from_json(filename)

            if not status:
                print(keywords)
                return

        except Exception as e:
            print(e)
            return

    elif textFile:
        pass
    else:
        raise Exception("File format not specified")

    # res = api.verify_credentials()    -----------> Doesn't work!

    streamListener = StreamListener.StreamListener()

    stream = tweepy.Stream(auth=api.auth, listener=streamListener)
    track_data = ["Chelsea AND F AND C", "Blues AND Chelsea",
                  "UEFA AND Chelsea", "Goal Chelsea"]

    a = stream.filter(track=track_data, languages="en", is_async=True)

    input("Press any key to exit...")

    print(a)
