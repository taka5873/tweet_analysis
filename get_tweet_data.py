import tweepy


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


# ツイート取得
def get_tweets(request):
    tw_id = request.POST["tweet_id"]
    import time
    start = time.time()

    tweet_data = []
    tw_res= tweepy.Cursor(api.user_timeline, screen_name=tw_id, exclude_replies=True)
    for tweet in tw_res.items(20):
        tweet_data.append(tweet.text.replace('\n', ''))
    print("tw", time.time() - start)
    return tweet_data


