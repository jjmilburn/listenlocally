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
    logger.info(kim_key)
    r = json.load(urllib.urlopen(
        "https://www.kimonolabs.com/api/25fjm8zy?apikey={}".format(kim_key)))

    spot_id = ''
    artist_spot_ids = []
    for local_show in r['results']['collection1']:
        artist_name = urllib.pathname2url((local_show['artist']['text']).encode("utf-8"))
        # in the future, we can break on these delimiters, and
        # treat each artist separately
        if ('&' not in artist_name and
                '+' not in artist_name and
                ',' not in artist_name):
            try:
                spot_artists = json.load(urllib.urlopen(
                    "https://api.spotify.com/v1/search?q={}&type=artist".format(
                        artist_name)))
            except IOError:
                logger.error("Problem with Spotify API Access")
            try:
                spot_id = spot_artists['artists']['items'][0]['id']  # 1st hit
                if not spot_id in artist_spot_ids:
                    artist_spot_ids.append(spot_id)
            except KeyError:  # no search results
                logger.warning(
                    "No Artist {} found in Spotify".format(artist_name))
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
                [0])
        except IndexError:  # no top tracks available?
            logger.warning(
                "No top tracks for spot_id".format(spot_id))
             #the actual track URL is
#            artist_top_tracks[x]['external_urls']['spotify'], launches
#https player for spotify song
    final_html_response = '<head><title>ListenLocally</title>' + \
            '<header><h1>Music By Artists Playing in SF Bay</h1></header>'

    ### this section is to be replaced with an actual HTML5 player.
    #  Open question: what is the Right Way to model this in Django?
    #  1. Get the data from Spotify (do it every time now)
    #  2. Store the data somehow (in a model in sqlite3; with a date?)
    #  3. Pull from the database and fill the html5 playlist
    #  Ideally, users can 'like' a track, and we can track this somehow.
    #  (separate question - session tracking)
    for top_track in artist_top_tracks:
        final_html_response = final_html_response + \
            '<audio controls preload="none">' + '<source src=\"' + \
            top_track['preview_url'] + '\">' + \
            ' type=\"audio/mpeg\"></audio>' + \
            ' ' + top_track['name'] + '</a>' + ' by ' + \
            top_track['artists'][0]['name'] + ' ' \
            '<a href=\"' + top_track['external_urls']['spotify'] + '\">' + \
            'Full Track Link' + '</a><br>'

    return HttpResponse('<pre>'+final_html_response+'</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

