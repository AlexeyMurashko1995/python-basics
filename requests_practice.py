import requests

url = 'https://catfact.ninja/fact'

response = requests.get(url)

if response.ok:
    data = response.json()
    print(f'Interesting fact: {data['fact']}')