
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from tabulate import tabulate


begin_date = dt.date(2020,2,15)
end_date = dt.date(2020,3,14)

lim = 3
lang = 'english'

tweets = query_tweets("coronavirus (from:NYTimes)",begindate= begin_date,enddate=end_date,limit=lim,lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv("RawTweets/LikelyNR/Raw/NBC.csv")

print(tabulate(df, headers='keys', tablefmt='psql'))