import requests
from pprint import pprint

def test_request():
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    superhero = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
    for hero in superhero:
        URL = requests.get(url + hero['name'])
        hero['intelligence'] = (URL.json()['results'][0]['powerstats']['intelligence'])
    print(sorted(superhero, key=lambda hero: hero['intelligence'])[0]["name"])

if __name__ == '__main__':
    test_request()

