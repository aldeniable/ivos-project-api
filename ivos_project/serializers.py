from rest_framework import serializers
from .models import SinglesStats
class SinglesStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglesStats
        fields = ['number_10_18_23_streams','album_id','title','artist_id']
 