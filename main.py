import csv
import json



def write_to_csv(row):
    with open('data1.csv', 'a+', encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row)


tweets = []
for line in open('CovidTweets.json', 'r'):
    tweets.append(json.loads(line))

for tweet in tweets:
    data = json.loads(json.dumps(tweet))
    tweet_id = data["id"]
    tweet_text = data["text"]
    user_id = data["user"]["id"]
    screen_name = data["user"]["screen_name"]
    in_reply_to_user_id = data["in_reply_to_user_id"]
    in_reply_screen_name = data["in_reply_to_screen_name"]
    write_to_csv([tweet_id, tweet_text, user_id, screen_name,in_reply_to_user_id, in_reply_screen_name])












