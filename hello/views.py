from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import urllib
import json
import os
import logging

# Create your views here.
def index(request):
    logger = logging.getLogger(__name__)
    kim_api = '25fjm8zy'  #in future, can change this
    kim_key = os.environ.get('KIMONO_KEY')
    r = json.load(urllib.urlopen(
        "https://www.kimonolabs.com/api/25fjm8zy?apikey={}".format(kim_key)))

    spot_id = ''
    artist_spot_ids = []
    for local_show in r['results']['collection1']:
        artist_name = local_show['artist']['text']

        # in the future, we can break on these delimiters, and
        # treat each artist separately
        if ('&' not in artist_name and
                '+' not in artist_name and
                ',' not in artist_name):
            try:
                spot_artists = json.load(urllib.urlopen(
                    "https://api.spotify.com/v1/search?q={}&type=artist".format(
                        artist_name.replace(" ", "%20"))))
            except IOError:
                logger.error("Problem with Spotify API Access")
            try:
                spot_id = spot_artists['artists']['items'][0]['id']  # 1st hit
                artist_spot_ids.append(spot_id)
            except IndexError:  # no artist found for this search.
                logger.warning(
                    "No Artist {} found in Spotify".format(artist_name))

    #now, loop through the artists, and get the top track for each.
    artist_top_tracks = []
    for spot_id in artist_spot_ids:
        try:
            top_tracks = json.load(urllib.urlopen(
                "https://api.spotify.com/v1/artists/{}/top-tracks?country=US".
                format(spot_id)))
        except IOError:
            logger.error(
                "Problem with Spotify API Access")
        try:
            artist_top_tracks.append(
                top_tracks['tracks']
                [0]
                ['external_urls']
                ['spotify'])
        except IndexError:  # no top tracks available?
            logger.warning(
                "No top tracks for spot_id".format(spot_id))
             #the actual track URL is
#            artist_top_tracks[x]['external_urls']['spotify'], launches
#https player for spotify song
    return HttpResponse('<pre>' + ', '.join(artist_top_tracks) + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

