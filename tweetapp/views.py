from django.shortcuts import render
import io
import urllib, base64
from get_tweet_data import get_tweets
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from tweetapp.bq import UpDownLoad, ipaexg_PATH
import requests
import json

load = UpDownLoad()


# Create your views here.

def index(request):
    return render(request, "tweetapp/index.html")


def get_wordcloud_img(request):
    tw_id = request.POST["tweet_id"]
    url = f"https://us-central1-instant-icon-250708.cloudfunctions.net/tw_analysis?message={tw_id}"
    res = requests.get(url)
    image_64 = res.content.decode()
    return render(request, "tweetapp/index.html", {"img": image_64})
