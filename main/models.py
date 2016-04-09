from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


#A list of the available local regions to search for
#Modelled after the craigslist regions?
#Eventually can actually link these back to kimono parsed URLS for
#each city on SongKick.
class localRegion(models.Model):
    SFBAY = 'SFBAY'
    CLEVELAND = 'CLEVELAND'
    REGION_FOR_MUSIC_CHOICES = (
        (SFBAY, 'SF Bay Area'),
        (CLEVELAND, 'Cleveland'),
    )
    region_name = models.CharField(max_length=30,
                                choices=REGION_FOR_MUSIC_CHOICES,
                                default=SFBAY)
    kimono_music_shows_url = models.URLField()
    
    #def getkimonoURLforRegion
    def __unicode__(self):
        return self.REGION_FOR_MUSIC_CHOICES


# A list of the local top track URL
# Possibly create a playlist at some point too?
# https://developer.spotify.com/web-api/create-playlist/
class LocalTopTracks(models.Model):
    region_name = models.CharField(max_length=30)

    def __unicode__(self):
        return "TOIMPLEMENT"


#  If an artist already exists, we can avoid hitting the spot API maybe
class ArtistTrackPair(models.Model):
    artist_name = models.CharField(max_length=255)
    artist_spot_id = models.CharField(max_length=30)
    artist_spot_uri = models.URLField()
    top_track_name = models.CharField(max_length=255)
    top_track_spot_id = models.CharField(max_length=30)
    top_track_spot_uri = models.URLField()
    top_track_spot_url = models.URLField()
    num_occurrences = models.IntegerField()  # how many shows?
    last_updated = models.DateField()

    def __unicode__(self):
        return "TOIMPLEMENT"


# other ideas:
# represent a list of 'liked' tracks?
# genre of given tracks?
#  Represent 'liked' tracks with this list?
