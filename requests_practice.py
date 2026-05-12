import requests

url = 'https://api.agify.io/'

params = {'name': 'Alex'}

response = requests.get(url, params=params)

if response.ok:
    data = response.json()
    print(f'Age: {data['age']}')
