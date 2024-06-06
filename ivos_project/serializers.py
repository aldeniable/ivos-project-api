from rest_framework import serializers
from .models import SinglesStats, Dates, Artist, Post, Post2, Timeline, Likes, UserProfile
from django.contrib.auth.models import User

class TopStreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglesStats
        fields = ['singles_stats_id','max_fetch_data_streams','album_name','title','artist_name','fetch_data_dates_id']

class TopTrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglesStats
        fields = ['singles_stats_id','difference_streams','album_name','title','artist_name']

class TopTrendingDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields = ['fetch_data_dates_id','fetch_dates']

class ConsistentFanScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_id','artist_name','consistent_fans_score', 'song_count', 'total_streams', 'onemil', 'fivemil', 'tenmil', 'fiftymil','hundredmil']

class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ['idPost','username', 'userID','datePosted','post','like_count']
class InsertPostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post2
            fields = ['username', 'userID','datePosted','post']
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username','password','email']

class TimelineSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Timeline
        fields = ['timeline_id', 'date' ,'title' , 'deets']

class LikesSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Likes
        fields = ['post_id' ,'user_id']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserProfile
        fields = ['id','username','email','fullname','age','place','fav_artist','fave_album','current_fave_song','gatekeep_song','fan_converter_song','alltime_fave_song','dont_like_song']