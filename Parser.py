import pandas as pd

df = pd.read_csv('RawTweets/LikelyNR/Raw/NBC.csv')

types =[]
texts =[]
likes =[]
retweets =[]
replies =[]
urls =[]

df_text = df.text
df_url = df.tweet_url
df_likes = df.likes
df_retweets = df.retweets
df_replies = df.replies

for text in df_text:
    text = (str)(text.encode('utf8').strip())
    text = text[2:-1]
    text = text.replace('http', ' http')
    texts+=[text]
    types+=['nr']
for url in df_url:
    urls+=['twitter.com'+url]
for like in df_likes:
    likes += [(str)(like)]
for retweet in df_retweets:
    retweets += [(str)(retweet)]
for reply in df_replies:
    replies +=[(str)(reply)]

ttu = zip(types,texts,likes, retweets,replies,urls)

df_out = pd.DataFrame(ttu, columns=['type','text','likes','retweets','num_comments','url'])

df_out.to_csv("RawTweets/LikelyNR/TextOnly/NBC.csv")