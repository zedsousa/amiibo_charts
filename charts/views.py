from django.http import HttpResponse
from django.shortcuts import render

from urllib.request import urlopen
import json
import requests
import pandas as pd


def index(request):
    response = requests.get("http://localhost:8000/amiibo/amiibo_list")

    data = json.loads(response.text)
    df = pd.json_normalize(data)

    df2 = df.groupby('gameSeries').count()
    df2 = df2.rename(columns={"amiiboSeries": "quantity"})
    df2 = df2[['quantity']]
    result2 = df2.to_json(orient="index")
    parsed2 = json.loads(result2)
    dump2 = json.dumps(parsed2)
    for data in parsed2:
        print(data)  

    return render(request, 'index.html', {'retorno': dump2})

def gameSeries(request):
    response = requests.get("http://localhost:8000/amiibo/amiibo_list")

    data = json.loads(response.text)
    df = pd.json_normalize(data)

    df2 = df.groupby('gameSeries').count()
    df2 = df2.rename(columns={"amiiboSeries": "quantity"})
    df2 = df2[['quantity']]
    result2 = df2.to_json(orient="index")
    parsed2 = json.loads(result2)
    dump2 = json.dumps(parsed2)
    for data in parsed2:
        print(data)  

    return render(request, 'index.html', {'retorno': dump2})

def amiiboSeries(request):
    response = requests.get("http://localhost:8000/amiibo/amiibo_list")

    data = json.loads(response.text)
    df = pd.json_normalize(data)

    df2 = df.groupby('amiiboSeries').count()
    df2 = df2.rename(columns={"gameSeries": "quantity"})
    df2 = df2[['quantity']]
    result2 = df2.to_json(orient="index")
    parsed2 = json.loads(result2)
    dump2 = json.dumps(parsed2)
    for data in parsed2:
        print(data)  

    return render(request, 'index.html', {'retorno': dump2})