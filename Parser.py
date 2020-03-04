import pandas as pd

df = pd.read_csv('RawTweets/LikelyR/Raw/bioweapon.csv')

types =[]
texts =[]
urls =[]

df_text = df.text
df_url = df.tweet_url

for text in df_text:
    texts+=[text.strip()]
    types+=['r']
for url in df_url:
    urls+=['twitter.com'+url]

ttu = zip(types,texts,urls)

df_out = pd.DataFrame(ttu, columns=['type','text','url'])

df_out.to_csv("RawTweets/LikelyR/TextOnly/bioweapon.csv")