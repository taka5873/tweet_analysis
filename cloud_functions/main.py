import tweepy
import time
import io
from datetime import datetime, timedelta
import urllib, base64
import pandas as pd
# import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
from janome.tokenizer import Tokenizer
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from bq import UpDownLoad

# from bq import UpDownLoad

t = Tokenizer()

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
def get_tweets(msg):
    tw_id = msg
    start = time.time()

    tweet_data = []
    tw_res = tweepy.Cursor(api.user_timeline, screen_name=tw_id, exclude_replies=True)
    for tweet in tw_res.items(20):
        tweet_data.append(tweet.text.lower().replace('\n', '').replace('https', '').replace('co', ''))
    print("tw", time.time() - start)
    return tweet_data


def main(request):
    words = []
    msg = request.args.get("message")
    # msg = "AbeShinzo"
    tweet_data = get_tweets(msg)
    for row in tweet_data:
        tokens = t.tokenize(row)
        for token in tokens:
            partOfSpeech = token.part_of_speech.split(',')[0]
            # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
            if partOfSpeech in ["名詞", "動詞", "形容詞", "副詞"]:
                words.append(token.surface)

    # # wordcloudで出力するフォントを指定
    ipaexg = "./ipaexg.ttf"
    ipaexg_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), ipaexg)
    font_path = ipaexg_PATH
    txt = " ".join(words)

    # 解析した単語、ストップワードを設定、背景の色は黒にしてます
    stop_words = [u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
                  u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した', u'思う', \
                  u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て', u'に', u'を', u'は', u'の', u'が', u'と', u'た', u'し', u'で', \
                  u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'', 'https', 'co']
    wordcloud = WordCloud(background_color="black", font_path=font_path,
                          stopwords=set(stop_words),
                          width=800, height=600).generate(txt)

    plt.imshow(wordcloud)
    plt.axis("off")
    image = io.BytesIO()  # image.read()は一度しか使えない
    plt.savefig(image, format='png')
    image.seek(0)
    # string = base64.b64encode(image.read())

    print("load")
    load = UpDownLoad()
    data = image.read()
    d = datetime.today() + timedelta(hours=9)
    d2 = (datetime.today() + timedelta(hours=9)).strftime("%Y-%m-%d_%H:%M:%S")
    bucket_name = "my_word_cloud3485"
    folder_name = f"{d.month}/{d.day}"
    file_name = f"wordcloud_{msg}_{d2}.png"
    res_gcs = load.data2gcs(data, bucket_name, folder_name, file_name)
    url = f"https://storage.cloud.google.com/{bucket_name}/{folder_name}/{file_name}?hl=ja"
    print(res_gcs)
    return url, 200

    # print(url)

    # image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)

    # return tweet_data

# print(main())
