from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
import os


# Create your views here.
def index(request):
    kimono_key = int(os.environ.get('KIMONO_KEY'))
    r = requests.get(
        'http://www.kimonolabs.com/api/25fjm8zy?apikey={}'.format(kimono_key))
    print r.text
    return HttpResponse(('<pre>' + r.text + '</pre>'))


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

