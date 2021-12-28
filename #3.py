import requests, pprint
from pprint import pprint
import datetime

def get_questions(days, tag):
    first_date = datetime.date.today()
    past_date = datetime.date.today() - datetime.timedelta(days=2)
    params = {'fromdate': past_date,
              'todate': first_date,
              'tagged': tag,
              'site': 'stackoverflow'}
    response = requests.get(url='https://api.stackexchange.com/2.3/questions', params=params)
    # pprint(response.json())
    for question in response.json().get('items'):
        print(('Question:' + question['title']).upper())
        print('Tags: ' + str(question['tags']))
        print('-' * 50)

get_questions(2, 'python')
