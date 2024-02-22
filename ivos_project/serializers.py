from rest_framework import serializers
from .models import SinglesStats

class TopStreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglesStats
        fields = ['singles_stats_id','max_fetch_data_streams','album_name','title','artist_name','fetch_data_dates_id']

class TopTrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglesStats
        fields = ['singles_stats_id','difference_streams','album_name','title','artist_name']
