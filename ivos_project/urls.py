
from django.contrib import admin
from django.urls import path, re_path
from .views import topStreams, topTrending, topTrendingDates, consistentFansScore, login, signup, testToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topStreams/', topStreams ),
    path('topTrending/', topTrending),
    path('topTrendingDates/', topTrendingDates),
    path('artistAnalytics/', consistentFansScore),
    path('login/', login),
    path('signup/', signup),
    path('testToken/', testToken)
    
]
