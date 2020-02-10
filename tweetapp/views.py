from django.shortcuts import render
import io
import urllib, base64
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# from tweetapp.bq import UpDownLoad, ipaexg_PATH
import requests
import json
from tweetapp.bq import UpDownLoad
import pandas as pd


# Create your views here.

def index(request):
    return render(request, "tweetapp/index.html")


def get_wordcloud_img(request):
    tw_id = request.POST["tweet_id"]
    url = f"https://us-central1-instant-icon-250708.cloudfunctions.net/tw_analysis?message={tw_id}"
    res = requests.get(url)
    # res = "https://storage.cloud.google.com/mytweet_840/wordcloud_img/wordcloud.png?hl=ja"
    image_64 = res.content.decode()
    # image_64 = "https://storage.cloud.google.com/mytweet_840/wordcloud_img/wordcloud.png?hl=ja"
    # query =
    new_tw_id = f"@{tw_id}"


    return render(request, "tweetapp/index.html", {"img": image_64, "new_tw_id": new_tw_id})

def show_picture(request,gcs_url):
    return render(request,"tweetapp/index2.html",{"img":gcs_url})
