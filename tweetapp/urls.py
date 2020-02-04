from django.urls import path,include
from .import views

app_name = "tweetapp"

urlpatterns = [
    path('',views.index, name='index'),
    path('get_tweet_id/',views.get_tweet_id,name="get_tweet_id")
]