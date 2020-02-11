from django.urls import path, include
from . import views

app_name = "tweetapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('get_wordcloud_img/', views.get_wordcloud_img, name="get_wordcloud_img"),
    path(r"tw_request/<path:imgur_url>/", views.show_picture,
         name="tw_request")
]
