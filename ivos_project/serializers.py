from rest_framework import serializers
from .models import SinglesStats, Dates, Artist, Post, Timeline, Likes
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
            fields = ['idPost','username', 'userID','datePosted','post']
            read_only_fields = ['idPost']
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
        fields = ['likes_id', 'post_id' ,'user_id']