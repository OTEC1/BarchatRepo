import collections
import configparser
import json
import requests

actors = []
actor = []


def barChart():
    global data
    responses = apicall("https://data-imdb1.p.rapidapi.com/actors", 1, getKey(1))

    for n in responses.json().get('results'):
        data = apicall(f"https://data-imdb1.p.rapidapi.com/actor/id/{n['nconst']}/awards/", 2, getKey(2))

    for d in data.json().get('results'):
        for q in d['actor']:
            actors.append(count(q['name'], d['year'], "", 1))
    for k, v in counter(actors).items():
        maps = json.loads(k)
        actor.append(count(maps['actor'], maps['year'], v, 2))
    print(actor)
    #ok


def counter(param):
    e = collections.Counter(param)
    return e


def count(param1, param2, param3, n):
    if n == 2:
        c = {"actor": param1, "year": param2, "award_count": param3}
    else:
        c = {"actor": param1, "year": param2}

    return json.dumps(c)


def getKey(n):
    config = configparser.ConfigParser()
    config.read('config.properties')

    if n == 1:
        c = config.get("Configclass", "rapid1")
    else:
        c = config.get("Configclass", "rapid2")

    return c


def apicall(n, i, key):
    if i == 1:
        query = {"limit": "50", "page": "1"}
    else:
        query = {"page_size": "30"}

    header = {
        'x-rapid-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    respones = requests.request("GET", n, headers=header, params=query)

    return respones


barChart()
