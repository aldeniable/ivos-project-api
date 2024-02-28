from django.http import JsonResponse
from .models import SinglesStats, Dates
from .serializers import TopStreamsSerializer, TopTrendingSerializer, TopTrendingDatesSerializer


def topStreams(request):
    singlesstats = SinglesStats.top_streams()
    serializer = TopStreamsSerializer(singlesstats, many = True)
    return JsonResponse(serializer.data, safe = False)

def topTrending(request):
    toptrending = SinglesStats.top_trending()
    serializer_toptrending = TopTrendingSerializer(toptrending, many = True)
    return JsonResponse(serializer_toptrending.data, safe = False)

def topTrendingDates(request):
    toptrendingdates = Dates.toptrendingdates()
    serializer_toptrendingdates = TopTrendingDatesSerializer(toptrendingdates, many = True)
    return JsonResponse(serializer_toptrendingdates.data, safe = False)
