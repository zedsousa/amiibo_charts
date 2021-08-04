from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen
import json
import requests

def index(request):
    response = requests.get("https://thingspeak.com/channels/196384/fields/1?results=500")

    data = json.loads(response.text)

    return render(request, 'index.html', {'retorno': data})

