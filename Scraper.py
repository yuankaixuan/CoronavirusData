
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from tabulate import tabulate


begin_date = dt.date(2020,2,1)
end_date = dt.date(2020,3,4)

lim = 100
lang = 'english'

tweets = query_tweets("coronavirus bioweapon",begindate= begin_date,enddate=end_date,limit=lim,lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv("RawTweets/LikelyR/Raw/bioweapon.csv")

print(tabulate(df, headers='keys', tablefmt='psql'))