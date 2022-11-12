import csv
import json



def CreateNetwork(user, user_reply_to, first: bool):
    with open('network_iatrounick.csv', mode='a+') as net:
        net_writer = csv.writer(net, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if first:
            net_writer.writerow(["user", "reply_to"])
        net_writer.writerow([user, user_reply_to])


ifFirst = True
empty = ''
tweets = []
for line in open('CovidTweets.json', 'r'):
    tweets.append(json.loads(line))

for tweet in tweets:
    data = json.loads(json.dumps(tweet))
    user_id = data["user"]["id"]
    in_reply_to_user_id = data["in_reply_to_user_id"]
    if data.get("in_reply_to_user_id"):
        CreateNetwork(user_id, in_reply_to_user_id, ifFirst)
    ifFirst = False

with open('network_iatrounick.csv') as f:
    # csv , delimited to txt tab del
    with open('userToUser.txt', 'w', newline='') as outputFile:
        r = csv.DictReader(f, delimiter=',')
        wr = csv.DictWriter(outputFile, r.fieldnames, delimiter='\t')
        wr.writeheader()
        wr.writerows(r)
