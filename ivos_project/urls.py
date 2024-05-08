
from django.contrib import admin
from django.urls import path, re_path
from .views import topStreams, topTrending, topTrendingDates, consistentFansScore, login, signup, posts, insertPost, timeline, didLike, likePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topStreams/', topStreams ),
    path('topTrending/', topTrending),
    path('topTrendingDates/', topTrendingDates),
    path('artistAnalytics/', consistentFansScore),
    path('login/', login),
    path('signup/', signup),
    path('posts/', posts),
    path('insertPost/', insertPost),
    path('timeline/', timeline),
    path('didLike/<int:userID>', didLike),
    path('likePost/<int:userID>/<int:postID>',likePost)
]
