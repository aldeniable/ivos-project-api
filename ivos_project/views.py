from django.http import JsonResponse
import models
from .serializers import SinglesStatsSerializer
def singles_stats(request):
