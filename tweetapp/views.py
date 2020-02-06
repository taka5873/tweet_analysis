from django.shortcuts import render
import io
import urllib, base64
from get_tweet_data import get_tweets
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from tweetapp.bq import UpDownLoad, ipaexg_PATH

load = UpDownLoad()


# Create your views here.

def index(request):
    return render(request, "tweetapp/index.html")


def get_wordcloud_img(request):
    tweet_data = get_tweets(request)
    mecab = MeCab.Tagger("-Ochasen")
    words = []
    # Mecabで形態素解析を実施
    for text in tweet_data:
        node = mecab.parseToNode(text)
        while node:
            word_type = node.feature.split(",")[0]

            # 取得する単語は、"名詞", "動詞", "形容詞", "副詞"
            if word_type in ["名詞", "動詞", "形容詞", "副詞"]:
                words.append(node.surface)

            node = node.next

    # # wordcloudで出力するフォントを指定
    font_path = ipaexg_PATH

    txt = " ".join(words)

    # 解析した単語、ストップワードを設定、背景の色は黒にしてます
    wordcloud = WordCloud(background_color="black", font_path=font_path,
                          width=800, height=600).generate(txt)

    plt.imshow(wordcloud)
    plt.axis("off")
    image = io.BytesIO()  # image.read()は一度しか使えない
    plt.savefig(image, format='png')
    image.seek(0)
    string = base64.b64encode(image.read())
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)

    return render(request, "tweetapp/index.html", {"img": image_64})
