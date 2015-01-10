from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import urllib
import json
import os


# Create your views here.
def index(request):
    kim_api = '25fjm8zy'
    kim_key = os.environ.get('KIMONO_KEY')
    r = json.load(urllib.urlopen(
        "https://www.kimonolabs.com/api/25fjm8zy?apikey={}".format(kim_key)))

    spot_id = ''
    artist_names = []
    for local_show in r['results']['collection1']:
        artist_name = local_show['artist']['text']
        if ('&' not in artist_name and
                'and' not in artist_name and
                ',' not in artist_name):
            try:
                spot_artists = json.load(urllib.urlopen(
                    "https://api.spotify.com/v1/search?q={}&type=artist".format(
                        artist_name.replace(" ", "%20"))))

                spot_id = spot_artists['artists']['items'][0]['id']  # 1st hit
            except:
                print "nope"
            print spot_id + '<br>'
            print local_show['artist']['text']
            artist_names.append(artist_name)
    return HttpResponse('<pre>' + ', '.join(artist_names) + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

