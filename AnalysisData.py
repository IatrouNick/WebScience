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

# import the graph as an edge list
G = nx.read_edgelist("userToUser.txt")
G.nodes
G.edges

# print the obvious
print('#nodes=', G.number_of_nodes())
print('#edges=', G.number_of_edges())

# print the conneted components
print('Size of connected components')
comp = list(nx.connected_components(G))
print('#Connected components', len(comp))
# for compLen in comp:
# S    print('size=', len(compLen))

# degree centrality
degreeNodes = dict(nx.degree(G))

tweets = []
for line in open('CovidTweets.json', 'r'):
    tweets.append(json.loads(line))
# save it
with open('degree.data', 'w') as f:
    w = csv.writer(f)
    w.writerows(degreeNodes.items())

top_10_degree = []
i = 0
sorted_degreeNodes = dict(sorted(degreeNodes.items(), key=lambda item: item[1], reverse=True))

for k, v in sorted_degreeNodes.items():
    k = int(k)

    degree_row = [k, v]
    if i != 10:
        found = False
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

        my_stop_words = text.ENGLISH_STOP_WORDS.union(['covid', 'corona'])
        # stop_words = set(stopwords.words('english'))
        vectorizer = TfidfVectorizer(stop_words=my_stop_words)
        vectorizer.fit([corpus])
        features = np.array(vectorizer.get_feature_names())
        corpus_vec = vectorizer.transform([corpus]).toarray()
        # find k-th largest indexes elements in each vector
        k1 = 5
        # take the last k-elements starting from the last
        indexes0 = corpus_vec[0, :].argsort()[-k1:][::-1]
        print('Tags: user', i + 1, name , features[indexes0])
        # top_10_degree.append(screen_name)
        if not found:
            top_10_degree.append(degree_row)
        i += 1

print("TOP 10 DEGREE", top_10_degree)

# find the pagerank centrality of the nodes of the Graphs
pgNodes = nx.pagerank(G)
# save it
with open('pageRank2.data', 'w') as f:
    w = csv.writer(f)
    w.writerows(pgNodes.items())

top_10_PageRanks = []
i = 0
sorted_pgNodes = dict(sorted(pgNodes.items(), key=lambda item: item[1], reverse=True))
for k, v in sorted_pgNodes.items():
    k = int(k)
    page_row = [k, v]
    if i != 10:
        found = False
        for tweet in tweets:
            data = json.loads(json.dumps(tweet))
            if k == data["user"]["id"]:
                screen_name = data["user"]["screen_name"]
                name = data["user"]["screen_name"]
                top_10_PageRanks.append(screen_name)
                top_10_PageRanks.extend(page_row)
                corpus = data["text"]
                found = True
                break
            elif k == data["in_reply_to_user_id"]:
                in_reply_screen_name = data["in_reply_to_screen_name"]
                name = data["in_reply_to_screen_name"]
                top_10_PageRanks.append(in_reply_screen_name)
                top_10_PageRanks.extend(page_row)
                corpus = data["text"]
                found = True
                break
        my_stop_words = text.ENGLISH_STOP_WORDS.union(['covid', 'corona'])
        # stop_words = set(stopwords.words('english'))
        vectorizer = TfidfVectorizer(stop_words=my_stop_words)
        vectorizer.fit([corpus])
        features = np.array(vectorizer.get_feature_names())
        corpus_vec = vectorizer.transform([corpus]).toarray()
        # find k-th largest indexes elements in each vector
        k2 = 5
        # take the last k-elements starting from the last
        indexes0 = corpus_vec[0, :].argsort()[-k2:][::-1]
        print('Tags: user', i + 1, name, features[indexes0])

        # top_10_degree.append(screen_name)
        if not found:
            top_10_PageRanks.append(page_row)
        i += 1
print("TOP 10 PAGERANK", top_10_PageRanks)

# pg is a dictionary, thus it has a key and a value
# pgNodes['8974']

btNodes = nx.betweenness_centrality(G)
# and the betweeness centrality
with open('between.data', 'w') as f:
    w = csv.writer(f)
    w.writerows(btNodes.items())

top_10_bet = []
i = 0
sorted_btNodes = dict(sorted(btNodes.items(), key=lambda item: item[1], reverse=True))
for k, v in sorted_btNodes.items():
    k = int(k)
    bet_row = [k, v]
    if i != 10:
        found = False
        for tweet in tweets:
            data = json.loads(json.dumps(tweet))

            if k == data["user"]["id"]:
                screen_name = data["user"]["screen_name"]
                name = data["user"]["screen_name"]
                top_10_bet.append(screen_name)
                top_10_bet.extend(bet_row)
                corpus = data["text"]
                found = True
                break
            elif k == data["in_reply_to_user_id"]:
                in_reply_screen_name = data["in_reply_to_screen_name"]
                name = data["in_reply_to_screen_name"]
                top_10_bet.append(in_reply_screen_name)
                top_10_bet.extend(bet_row)
                corpus = data["text"]
                found = True
                break

        my_stop_words = text.ENGLISH_STOP_WORDS.union(['covid', 'corona'])
        # stop_words = set(stopwords.words('english'))
        vectorizer = TfidfVectorizer(stop_words=my_stop_words)
        vectorizer.fit([corpus])
        features = np.array(vectorizer.get_feature_names())
        corpus_vec = vectorizer.transform([corpus]).toarray()
        # find k-th largest indexes elements in each vector
        k3 = 5
        # take the last k-elements starting from the last
        indexes0 = corpus_vec[0, :].argsort()[-k3:][::-1]
        print('Tags: user', i + 1, name,  features[indexes0])
        # top_10_degree.append(screen_name)
        if not found:
            top_10_bet.append(bet_row)
        i += 1
print("TOP 10 between", top_10_bet)




