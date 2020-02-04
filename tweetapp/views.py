from django.shortcuts import render
from django.http import HttpResponse
# from get_tweet_data import get_tweets

# Create your views here.

def index(request):
    return render(request,"tweetapp/index.html")

def get_tweet_id(request):
    tw_id = request.POST["tweet_id"]
    # df = get_tweets()


    # return render(request,"tweetapp/index.html",{"tw_id":df.to_html()})
    return render(request,"tweetapp/index.html",{"tw_id":tw_id})
