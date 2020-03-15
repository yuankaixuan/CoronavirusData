from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

while True:
    with open('SortedTweets/SortedTweets.csv', 'a+', newline='') as f:
        url = input("Enter tweet URL, or stop to exit.")
        if url == 'stop':
           break;
        type = 'nr' # input("Enter r for rumor, or nr for non rumor")

        html = urlopen(url)
        soup = BeautifulSoup(html, features="html.parser")
        tweet_text = str(soup.find('p', {"class": 'tweet-text'}).text.encode('utf8').strip())
        tweet_text = tweet_text[2:-1]
        tweet_text = tweet_text.replace("http",' http')

        try:
            likes = str(soup.find('a', {"class": 'request-favorited-popup'}).text.encode('utf8').strip())
        except:
            likes = '0'
        else:
            likes = likes[2:-6]

        try:
            retweets = str(soup.find('a', {"class": 'request-retweeted-popup'}).text.encode('utf8').strip())
        except:
            retweets = '0'
        else:
            retweets = retweets[2:-9]

        try:
            num_comments = str(
                soup.find('span', {"class": 'ProfileTweet-actionCountForPresentation'}).text.encode('utf8').strip())
        except:
            num_comments='0'
        else:
            num_comments = num_comments[2:-1]



        row = [type,tweet_text,likes,retweets,num_comments,url]
        csv_writer = writer(f)
        csv_writer.writerow(row)

# r = requests.get(url)
# text_file = open("tweet.html", "wt", encoding='utf-8')
# n = text_file.write(r.text)
# text_file.close()
