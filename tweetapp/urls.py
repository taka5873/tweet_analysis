from django.urls import path,include
from .import views

app_name = "tweetapp"

urlpatterns = [
    path('',views.index, name='index'),
    path('get_wordcloud_img/', views.get_wordcloud_img, name="get_wordcloud_img")
    path(r"tw_analysis/<str:gcs_url>/", view.show_picture, name="tw_analysis")


https://storage.cloud.google.com/my_word_cloud3485/2/10/wordcloud_AbeShinzo_2020-02-10_20%3A55%3A03.png?hl=ja