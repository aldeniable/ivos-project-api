from django.http import JsonResponse
from .models import SinglesStats
from .serializers import SinglesStatsSerializer

def singles_stats(request):

    singlesstats = SinglesStats.display()
    serializer = SinglesStatsSerializer(singlesstats, many = True)
    return JsonResponse(serializer.data, safe = False)