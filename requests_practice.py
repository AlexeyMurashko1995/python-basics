import requests
import os
from dotenv import load_dotenv


# Task 1. Practising with a GET request (1 parameter)
url = 'https://api.agify.io/'

params = {'name': 'Alex'}

response = requests.get(url, params=params)

if response.ok:
    data = response.json()
    print(f'Age: {data['age']}')

# Task 2. Practising with APIs using multiple parameters

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

# Task 3. Working with API keys and headers (Secure connection)

load_dotenv()
api_key = os.getenv('API_NINJA_KEY')

url = 'https://api.api-ninjas.com/v1/facts'
headers = {'X-Api-Key': api_key}

response = requests.get(url, headers=headers)

if response.ok:
    data = response.json()
    print(f"Interesting fact: {data[0]['fact']}")