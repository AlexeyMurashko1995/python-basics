import requests

# # Task 1. Practising with request GET (1 param)
# url = 'https://api.agify.io/'

# params = {'name': 'Alex'}

# response = requests.get(url, params=params)

# if response.ok:
#     data = response.json()
#     print(f'Age: {data['age']}')

# Task 2. Practising with API using several params

url = 'https://api.open-meteo.com/v1/forecast'

params = {
    'latitude' : 52.23,
    'longitude' : 21.01,
    'current_weather' : True
}

response = requests.get(url, params=params)

if response.ok:
    data = response.json()
    print(data['current_weather']['temperature'])