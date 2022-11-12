# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:09:36 2020

source: https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
@author: dimitrv

you will need to install: Tweepy

 pip install tweepy
"""
import json

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
#from tweepy.streaming import StreamListener


consumer_key = '123'
consumer_secret = '123'
access_token = '123'
access_secret = ''123'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


class IDPrinter(tweepy.Stream):

    def on_status(self, status):

        json_str = json.dumps(status._json)

        print("id=", status.id)
        print("\n", type(status))
        print("\n", status)
        print("=============================")

        try:
            with open("data.json", "a") as f:
                f.write(json_str + "\n")
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))


class ConnectionTester(tweepy.Stream):
    def on_connection_error(self):
        self.disconnect()


stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_secret)

printer = IDPrinter(consumer_key, consumer_secret, access_token, access_secret)
printer.filter(track=["Covid-19","Covid","Coronavirus","Delta"])
