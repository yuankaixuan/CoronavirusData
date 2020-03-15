from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

df = pd.read_csv('RawTweets/LikelyNR/Raw/NBC.csv')

with open('SortedTweets/SortedTweets.csv', 'a+', newline='') as f:

    types =[]
    texts =[]
    likes =[]
    retweets =[]
    replies =[]
    urls =[]

    type = 'nr'
    df_text = df.text
    df_url = df.tweet_url
    df_likes = df.likes
    df_retweets = df.retweets
    df_replies = df.replies

    for text in df_text:
        text = (str)(text.encode('utf8').strip())
        text = text[2:-1]
        text = text.replace('http', ' http')
        texts += [text]
    for url in df_url:
        urls+=[(str)(url)]
    for like in df_likes:
        likes += [(str)(like)]
    for retweet in df_retweets:
        retweets += [(str)(retweet)]
    for reply in df_replies:
        replies +=[(str)(reply)]


    for i in range(len(texts)):
        tweet_text = texts[i];
        like = likes[i]
        retweet = retweets[i]
        num_comments = replies[i]
        url = urls[i]
        row = [type,tweet_text,like,retweet,num_comments,url]
        csv_writer = writer(f)
        csv_writer.writerow(row)

# r = requests.get(url)
# text_file = open("tweet.html", "wt", encoding='utf-8')
# n = text_file.write(r.text)
# text_file.close()
