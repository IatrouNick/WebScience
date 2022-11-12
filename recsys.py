import item as item
import networkx as nx
import stopwords as stopwords
from networkx.algorithms import community
import numpy as np
import csv
import matplotlib.pyplot as plt
import spicy as sp
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import nltk

tweets = []
for line in open('CovidTweets.json', 'r'):
    tweets.append(json.loads(line))

users = []
for line in open('network_iatrounick.csv', 'r'):
    users.append(line)
print(users)

for tweet in tweets:
    data = json.loads(json.dumps(tweet))
    # check for the id of the user add characteristic tags

    if k == data["user"]["id"]:
        screen_name = data["user"]["screen_name"]
        name = data["user"]["screen_name"]
        top_10_degree.append(screen_name)
        top_10_degree.extend(degree_row)
        corpus = data["text"]
        found = True
        break
    elif k == data["in_reply_to_user_id"]:
        in_reply_screen_name = data["in_reply_to_screen_name"]
        name = data["in_reply_to_screen_name"]
        top_10_degree.append(in_reply_screen_name)
        top_10_degree.extend(degree_row)
        corpus = data["text"]
        found = True
        break