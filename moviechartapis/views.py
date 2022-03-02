from django.shortcuts import render
import configparser
import json
import requests
import collections


def barchart(request):
    date = []
    names = []
    query = {"limit": "22", "page": "1"}
    header = {
        'x-rapid-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': getKey()
    }
    responses = requests.request("GET", "https://data-imdb1.p.rapidapi.com/actors", headers=header, params=query)
    for n in responses.json().get('results'):
        date.append(n['birthYear'])
        names.append(n['primaryName'])
    return render(request, 'moviechartapi/chart.html', {'count': date, 'Actor': names})


def getKey():
    config = configparser.ConfigParser()
    config.read('config.properties')
    return config.get("Configclass", "rapid")


