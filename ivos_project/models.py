from django.db import models, connection


class SinglesStats(models.Model):
    singles_stats_id = models.IntegerField(primary_key = True)
    artist_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    album_id = models.IntegerField(blank=True, null=True)
    fetch_data_dates_id = models.IntegerField(blank=True, null=True)
    max_fetch_data_streams = models.IntegerField(blank=True, null=True)
    difference_streams = models.IntegerField(blank = True, null = True)
    album_name = models.CharField(max_length=45, blank=True, null=True)
    artist_name = models.CharField(max_length=45, blank=True, null=True)
    fetch_dates = models.DateField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'singles_stats'
    #Alden 01-10-24: function to retrieve Top Streams
    def top_streams():
        query ="""
                SELECT
                    single.singles_stats_id,
                    single.title,
                    max_streams.subquery_streams AS max_fetch_data_streams,
                    single.fetch_data_dates_id,
                    artist.artist_name,
                    album.album_name
                FROM
                    singles_stats single
                INNER JOIN
                    artist ON single.artist_id = artist.artist_id
                LEFT JOIN
                    album ON single.album_id = album.album_id
                INNER JOIN (
                    SELECT
                        title,
                        MAX(fetch_data_dates_id) AS max_fetch_data_dates_id,
                        MAX(streams) AS subquery_streams
                    FROM
                        singles_stats
                    GROUP BY
                        title
                ) AS max_streams
                ON single.title = max_streams.title AND single.fetch_data_dates_id = max_streams.max_fetch_data_dates_id
                ORDER BY
                    single.streams DESC;
                """
        topstreams = SinglesStats.objects.raw(query)
        return topstreams

    #Alden 02-22-24: function to retrieve Top Trending
    def top_trending():
        query ="""

                SELECT
                    single.singles_stats_id,
                    single.title,
                    difference_streams.difference AS difference_streams,
                    artist.artist_name,
                    album.album_name
                FROM
                    singles_stats single
                INNER JOIN
                    artist ON single.artist_id = artist.artist_id
                LEFT JOIN
                    album ON single.album_id = album.album_id
                INNER JOIN (
					SELECT
					title,
					(
					SELECT
						streams
						FROM singles_stats s2
						WHERE s2.title = s1.title ORDER BY fetch_data_dates_id DESC LIMIT 1
					)
					-
					(
					SELECT
						streams
						FROM singles_stats s2
						WHERE s2.title = s1.title ORDER BY fetch_data_dates_id DESC LIMIT 1 OFFSET 1
					) as difference
					FROM singles_stats s1
					GROUP BY title
                ) AS difference_streams ON single.title = difference_streams.title
                WHERE single.singles_stats_id = (
					SELECT MAX(s2.singles_stats_id)
					FROM singles_stats s2
					WHERE s2.title = single.title
				)
			    ORDER BY difference_streams DESC;

                """
        toptrending = SinglesStats.objects.raw(query)
        return toptrending
    
class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    album_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'

class Timeline(models.Model):
    timeline_id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length = 100, blank=True, null=True)
    deets = models.CharField(max_length = 500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeline'

    def getAll():   #05-02-2024
        query = """
             SELECT * FROM timeline
             ORDER BY date DESC;
            """
        timelines = Timeline.objects.raw(query)
        return timelines

class Dates(models.Model):
    fetch_data_dates_id = models.IntegerField(primary_key=True)
    fetch_dates = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetch_data_dates'
    
    def toptrendingdates():
        query = """
                SELECT fetch_data_dates_id, fetch_dates FROM fetch_data_dates
                ORDER BY fetch_dates DESC
                LIMIT 2;
            """
        toptrendingdates = Dates.objects.raw(query)
        return toptrendingdates
    
class Post(models.Model):
    idPost = models.IntegerField(primary_key = True)
    userID = models.IntegerField()
    datePosted = models.DateTimeField(blank = True)
    post = models.TextField(blank = True)
    username = models.CharField(max_length = 150)
    like_count= models.BigIntegerField(null = True, blank = True)

    class Meta:
        managed = False
        db_table = 'posts'
    #04-23-2024 
    def getposts():
        query = """
                    SELECT
                    p.idPost,
                    p.username,
                    p.datePosted,
                    p.post,
                    (SELECT COUNT(*) FROM likes l WHERE l.post_id = p.idPost) AS like_count
                    FROM
                    posts p
                    ORDER BY
                    p.datePosted DESC;
            """
        posts = Post.objects.raw(query)
        return posts 
    
class Post2(models.Model):
    idPost = models.IntegerField(primary_key = True)
    userID = models.IntegerField()
    datePosted = models.DateTimeField(blank = True)
    post = models.TextField(blank = True)
    username = models.CharField(max_length = 150)

    class Meta:
        managed = False
        db_table = 'posts'


class Likes(models.Model):
    likes_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'likes'
    #05062024
    def didLike(userID):
        return Likes.objects.filter(user_id = userID)
        

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(max_length=45, blank=True, null=True)
    consistent_fans_score = models.CharField(max_length=45, blank=True, null=True)
    song_count = models.IntegerField(blank = True, null = True)
    total_streams = models.IntegerField(blank = True, null = True)
    onemil = models.IntegerField(blank = True, null = True)
    fivemil = models.IntegerField(blank = True, null = True)
    tenmil = models.IntegerField(blank = True, null = True)
    fiftymil = models.IntegerField(blank = True, null = True)
    hundredmil =models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'artist'























class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    class Meta:
        managed = False
        db_table = 'auth_group'
class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'django_admin_log'
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_migrations'
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

