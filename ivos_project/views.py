from django.http import JsonResponse
from .models import SinglesStats
from .serializers import TopStreamsSerializer, TopTrendingSerializer

def topStreams(request):
    singlesstats = SinglesStats.top_streams()
    serializer = TopStreamsSerializer(singlesstats, many = True)
    return JsonResponse(serializer.data, safe = False)

def topTrending(request):
    singlesstats = SinglesStats.top_trending()
    serializer = TopTrendingSerializer(singlesstats, many = True)
    return JsonResponse(serializer.data, safe = False)