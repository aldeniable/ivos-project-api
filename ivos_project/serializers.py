from rest_framework import serializers
import models
class SinglesStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SinglesStats
        fields = ['number_10_18_23_streams','album_id','title','artist_id']
