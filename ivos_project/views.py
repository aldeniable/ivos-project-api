from django.http import JsonResponse
from .models import SinglesStats, Dates, Post, Timeline
from django.contrib.auth.models import User
from .serializers import TopStreamsSerializer, TopTrendingSerializer, TopTrendingDatesSerializer, ConsistentFanScoreSerializer, UserSerializer, PostSerializer, TimelineSerializer
from statistics import stdev, mean
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

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

def timeline(request):
    timeline = Timeline.getAll()
    serializer = TimelineSerializer(timeline, many = True)
    return JsonResponse(serializer.data, safe = False)

def posts(request):
    posts = Post.getposts()
    serializer = PostSerializer(posts, many = True)
    return JsonResponse(serializer.data, safe = False)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def insertPost(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("P")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return Response({"token": token.key, "user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response ({"detail":"Not found."}, status = status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user = user) 
    serializer = UserSerializer(instance = user)   
    return Response({"token": token.key, "user":serializer.data})

def consistentFansScore(request):
    consistentFansScore = SinglesStats.top_streams()
    ivos, blaster, zild, unique = [],[],[],[]
    zild1mil, zild5mil, zild10mil, zild50mil, zild100mil = 0, 0, 0, 0, 0
    blaster1mil, blaster5mil, blaster10mil, blaster50mil, blaster100mil = 0, 0, 0, 0, 0
    unique1mil, unique5mil, unique10mil, unique50mil, unique100mil = 0, 0, 0, 0, 0
    ivos1mil, ivos5mil, ivos10mil, ivos50mil, ivos100mil = 0, 0, 0, 0, 0

    for entry in consistentFansScore:
        if entry.artist_name == 'IV OF SPADES':
            if entry.max_fetch_data_streams >= 1000000:
                ivos1mil += 1
            if entry.max_fetch_data_streams >= 5000000:
                ivos5mil += 1
            if entry.max_fetch_data_streams >= 10000000:
                ivos10mil += 1
            if entry.max_fetch_data_streams >= 50000000:
                ivos50mil += 1
            if entry.max_fetch_data_streams >= 100000000:
                ivos100mil += 1            
            ivos.append(entry.max_fetch_data_streams)
        elif entry.artist_name == 'Zild Benitez':
            if entry.max_fetch_data_streams >= 1000000:
                zild1mil += 1
            if entry.max_fetch_data_streams >= 5000000:
                zild5mil += 1
            if entry.max_fetch_data_streams >= 10000000:
                zild10mil += 1
            if entry.max_fetch_data_streams >= 50000000:
                zild100mil += 1    
            if entry.max_fetch_data_streams >= 100000000:
                zild100mil += 1     
            zild.append(entry.max_fetch_data_streams)
        elif entry.artist_name == 'Unique Salonga':
            if entry.max_fetch_data_streams >= 1000000:
                unique1mil += 1
            if entry.max_fetch_data_streams >= 5000000:
                unique5mil += 1
            if entry.max_fetch_data_streams >= 10000000:
                unique10mil += 1
            if entry.max_fetch_data_streams >= 50000000:
                unique50mil += 1
            if entry.max_fetch_data_streams >= 100000000:
                unique100mil += 1  
            unique.append(entry.max_fetch_data_streams)
        elif entry.artist_name == 'Blaster Silonga':
            if entry.max_fetch_data_streams >= 1000000:
                blaster1mil += 1
            if entry.max_fetch_data_streams >= 5000000:
                blaster5mil += 1
            if entry.max_fetch_data_streams >= 10000000:
                blaster10mil += 1
            if entry.max_fetch_data_streams >= 50000000:
                blaster50mil += 1
            if entry.max_fetch_data_streams >= 100000000:
                blaster100mil += 1  
            blaster.append(entry.max_fetch_data_streams)
        
    ivos_sum = sum(ivos)
    ivos_mean = mean(ivos)
    ivos_dev = stdev(ivos)
    ivos_COV = (ivos_dev/ivos_mean) * 100
    blaster_sum = sum(blaster)
    blaster_mean = mean(blaster)
    blaster_dev = stdev(blaster)
    blaster_COV = (blaster_dev/blaster_mean) * 100
    zild_sum = sum(zild)
    zild_mean = mean(zild)
    zild_dev = stdev(zild)
    zild_COV = (zild_dev/zild_mean)*100
    unique_sum = sum(unique)
    unique_mean = mean(unique)
    unique_dev = stdev(unique)
    unique_COV = (unique_dev/unique_mean) * 100
    fans_rate_zild = zild_COV / len(zild)
    fans_rate_ivos = ivos_COV / len(ivos)
    fans_rate_unique = unique_COV / len(unique)
    fans_rate_blaster = blaster_COV / len(blaster)
    arrayOfScores = [fans_rate_zild, fans_rate_blaster, fans_rate_ivos, fans_rate_unique]
    sortedScores = sorted(arrayOfScores)

    zild_rank = blaster_rank = ivos_rank = unique_rank = None
    rank_counter = 1
    for score in sortedScores:
        if score == fans_rate_zild:
            zild_rank = f'{rank_counter}'
        elif score == fans_rate_blaster:
            blaster_rank = f'{rank_counter}'
        elif score == fans_rate_ivos:
            ivos_rank = f'{rank_counter}'
        elif score == fans_rate_unique:
            unique_rank = f'{rank_counter}'
        rank_counter += 1
    
    consistentFansScores = [
        {'artist_id': 1,
         'artist_name': 'IV OF SPADES',
         'consistent_fans_score': ivos_rank,
         'song_count': len(ivos),
         'total_streams': ivos_sum,
         'onemil': ivos1mil,
         'fivemil': ivos5mil,
         'tenmil' : ivos10mil,
         'fiftymil' : ivos50mil,
         'hundredmil' : ivos100mil
        },
        {'artist_id': 2,
         'artist_name': 'Unique Salonga',
         'consistent_fans_score': unique_rank,
         'song_count': len(unique),
         'total_streams': unique_sum,
        'onemil': unique1mil,
         'fivemil': unique5mil,
         'tenmil' : unique10mil,
         'fiftymil' : unique50mil,
         'hundredmil' : unique100mil
        },
        {'artist_id': 3,
         'artist_name': 'Zild Benitez',
         'consistent_fans_score': zild_rank,
         'song_count': len(zild),
         'total_streams': zild_sum,
         'onemil': zild1mil,
         'fivemil': zild5mil,
         'tenmil' : zild10mil,
         'fiftymil' : zild50mil,
         'hundredmil' : zild100mil
        },
        {'artist_id': 4,
         'artist_name': 'Blaster Silonga',
         'consistent_fans_score': blaster_rank,
         'song_count': len(blaster),
         'total_streams': blaster_sum,
        'onemil': blaster1mil,
         'fivemil': blaster5mil,
         'tenmil' : blaster10mil,
         'fiftymil' : blaster50mil,
         'hundredmil' : blaster100mil
        }
    ]
    sorted_consistentFansScores = sorted(consistentFansScores, key=lambda x: x['consistent_fans_score'])
    serializer_consistentFanScore = ConsistentFanScoreSerializer(sorted_consistentFansScores, many = True)
    return JsonResponse(serializer_consistentFanScore.data, safe = False)