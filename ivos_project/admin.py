
from django.contrib import admin
from .models import Album
from .models import Artist
from .models import SinglesStats

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(SinglesStats)