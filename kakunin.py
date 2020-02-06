import MeCab
import pandas as pd

mecab = MeCab.Tagger("-Ochasen")

words=[]
df = pd.read_csv("./tweet_data.csv")
print(df.head())

