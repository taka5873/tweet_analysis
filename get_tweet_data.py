import pandas as pd
import tweepy
import datetime

# TweepyAPI KEY
CONSUMER_KEY = "czH2MU9FpfQJlaCOkXGgG6NOF"
CONSUMER_SECRET = "bQ5l0t7ypCkARf7PDdSWqWeogAi38emDoPb3UJChuasgvtYNLB"
ACCESS_TOKEN = "1067433150970654720-yiord2TbDdGjPto1KzqTv1lbQeJHtl"
ACCESS_TOKEN_SECRET = "D2wCmoiTDIdqYDIpbZFo32lPv3a7CUmEzsgJ6p5IaYtDL"
# tweepyの設定
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
columns_name = ["TW_NO", "TW_TIME", "TW_TEXT", "FAV", "RT"]
# ここで取得したいツイッターアカウントIDを指定する
# tw_id = "hayatakun52n5"


# ツイート取得
def get_tweets(request):
    tw_id = request.POST["tweet_id"]
    tweet_data = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=tw_id, exclude_replies=True).items(20):
        tweet_data.append([tweet.id, tweet.created_at + datetime.timedelta(hours=9), tweet.text.replace('\n', ''),
                           tweet.favorite_count, tweet.retweet_count])
    df = pd.DataFrame(tweet_data, columns=columns_name)
    return df

    # df.to_csv("./tweet_data1.csv")

    # print("end1")

