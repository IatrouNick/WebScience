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
#######################################
#######################################
#######################################
###       communities part         ####
tweets = []
for line in open('CovidTweets.json', 'r'):
    tweets.append(json.loads(line))
G = nx.read_edgelist("userToUser.txt")
# compute the local clustering coefficient for each node
lClustCoeff = nx.clustering(G)

# community detection
# with the clique percolation
# try higher values of k
k = 3
comms = list(nx.community.k_clique_communities(G, k))
print('number of communities=', len(comms))

# for c in comms:
#    print('comm size=', len(c))

# save the communities in a text file, one line per community


f2 = open('comms.data', 'w')
for c in comms:
    f2.write(','.join(list(c)))
    f2.write('\n')
f2.close()

user_coms = []
for x in comms:
    user_coms.append(list(x))

# get the top 10 communities based on size
top_10_coms = []

for j in range(0, 10):
    biggest_size = 0
    biggest_index = 0
    counter = 0

    for i in range(0, len(user_coms)):
        if len(user_coms[i]) > biggest_size and ([i + 1, user_coms[i]] not in top_10_coms):
            biggest_size = len(user_coms[i])
            biggest_index = i

    entry = [biggest_index + 1, user_coms[biggest_index]]


    if entry not in top_10_coms:
        top_10_coms.append(entry)
        print(entry)
        #find tags
        corpus:str= ''
        for user in user_coms[biggest_index]:
            user = int(user)

            for tweet in tweets:
                data = json.loads(json.dumps(tweet))

                if user == data["user"]["id"]:
                    corpus += data["text"]
                    found = True
                    break
                elif user == data["in_reply_to_user_id"]:
                    corpus += data["text"]
                    found = True
                    break

        my_stop_words = text.ENGLISH_STOP_WORDS.union(['covid', 'corona'])
        # stop_words = set(stopwords.words('english'))
        vectorizer = TfidfVectorizer(stop_words=my_stop_words)
        vectorizer.fit([corpus])
        features = np.array(vectorizer.get_feature_names())
        corpus_vec = vectorizer.transform([corpus]).toarray()
        # find k-th largest indexes elements in each vector
        k4 = 7
        # take the last k-elements starting from the last
        indexes0 = corpus_vec[0, :].argsort()[-k4:][::-1]
        print('Tags: community', [biggest_index + 1], features[indexes0])