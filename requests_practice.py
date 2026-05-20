import requests
import os
from dotenv import load_dotenv

# ==============================================================================
# Task 1. Practising with a GET request (1 parameter)
# ==============================================================================
# url = 'https://api.agify.io/'
# params = {'name': 'Alex'}
# response = requests.get(url, params=params)
# if response.ok:
#     data = response.json()
#     print(f'Age: {data['age']}')

# ==============================================================================
# Task 2. Practising with APIs using multiple parameters
# ==============================================================================
# url = 'https://api.open-meteo.com/v1/forecast'
# params = {
#     'latitude' : 52.23,
#     'longitude' : 21.01,
#     'current_weather' : True
# }
# response = requests.get(url, params=params)
# if response.ok:
#     data = response.json()
#     print(data['current_weather']['temperature'])

# ==============================================================================
# Task 3. Working with API keys and headers (Secure connection)
# ==============================================================================
# load_dotenv()
# api_key = os.getenv('API_NINJA_KEY')
# url = 'https://api.api-ninjas.com/v1/facts'
# headers = {'X-Api-Key': api_key}
# response = requests.get(url, headers=headers)
# if response.ok:
#     data = response.json()
#     print(f"Interesting fact: {data[0]['fact']}")

# ==============================================================================
# Task 4. GET + params (practice)
# ==============================================================================
# url = 'https://api.nationalize.io/'
# params = {'name':'Alex'}
# response = requests.get(url, params=params)
# if response.ok:
#     data = response.json()
#     print(data['country'][0])

# ==============================================================================
# Task 5. Zippopotam API
# ==============================================================================
# url = 'https://api.zippopotam.us/pl/00-001'
# response = requests.get(url)
# if response.ok:
#     data = response.json()
#     print(data['places'][0]['place name'])

# ==============================================================================
# Task 6. Double Query (Orchestration)
# ==============================================================================
# name = 'Alex'
# params = {'name': name}

# first_url = 'https://api.agify.io'
# second_url = 'https://api.genderize.io'

# first_response = requests.get(first_url, params=params)
# second_response = requests.get(second_url, params=params)

# if first_response.ok and second_response.ok:
#     first_data = first_response.json()
#     second_data = second_response.json()

#     # Using f-string to aggregate data from both sources
#     output = (
#         f"Name: {first_data['name']} | "
#         f"Age: {first_data['age']} | "
#         f"Gender: {second_data['gender']}"
#     )
#     print(output)

# ==============================================================================
# Task 7. Exception Handling
# ==============================================================================

# try:

#     name = 'Alex'
#     params = {'name': name}

#     first_url = 'https://api.agify.io'
#     second_url = 'https://api.genderize.io'

#     first_response = requests.get(first_url, params=params)
#     second_response = requests.get(second_url, params=params)

#     if first_response.ok and second_response.ok:
#         first_data = first_response.json()
#         second_data = second_response.json()

#         # Using f-string to aggregate data from both sources
#         output = (
#             f"Name: {first_data['name']} | "
#             f"Age: {first_data['age']} | "
#             f"Gender: {second_data['gender']}"
#         )
#         print(output)

# except requests.exceptions.ConnectionError:
#     print('Check your internet connection!')

# except requests.exceptions.Timeout:
#     print('The server does not respond!')

# ==============================================================================
# Task 8. POST request
# ==============================================================================

# try:
#     url = 'https://httpbin.org/post'

#     payload = {
#         'model': 'gemini - pro',
#         'prompt': 'Hello, AI!'
#     }

#     response = requests.post(url, json=payload)

#     if response.ok:
#         data = response.json()
#         print(data)

# except requests.exceptions.ConnectionError:
#     print('Check your internet connection!')

# except requests.exceptions.ConnectTimeout:
#     print('The server does not respond')

# ==============================================================================
# Task 9. Headers & The Secret Key
# ==============================================================================

# try:
#     url = 'https://httpbin.org/post'

#     payload = {
#         'model': 'gemini-pro',
#         'prompt': 'Hello, AI!'
#     }

#     headers = {
#         'Authorization': 'Bearer my-super-secret-python-ai-token-2026',
#         'Content-Type': 'application/json'
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     if response.ok:
#         data = response.json()
#         print(data['headers'])

# except requests.exceptions.ConnectionError:
#     print('Check your internet connection')

# except requests.exceptions.ConnectTimeout:
#     print('The server does not respond')

# ==============================================================================
# Task 10. Status Code Detective
# ==============================================================================

# try:
#     url = 'https://httpbin.org/status/404'

#     response = requests.get(url)

#     if response.status_code == 404:
#         print('The page is not found')

#     elif response.status_code == 200:
#         print('Success')

# except requests.exceptions.ConnectionError:
#     print('Check your internet connection')

# except requests.exceptions.ConnectTimeout:
#     print('The server does not respond')

# ==============================================================================
# Task 11. JSON Data Architect
# ==============================================================================
# import json

# raw_json = '{"user_id": 12, "role": "student", "skills": ["Python", "English"]}'

# raw_python = json.loads(raw_json)

# raw_python['skills'].append('AI Basics')
# raw_python['role'] = 'Python Developer'

# raw_json = json.dumps(raw_python, indent=4)

# print(raw_json)

# ==============================================================================
# Task 12. Nationality Analyzer (GET + Params + JSON)
# ==============================================================================

# try:
#     url = 'https://api.nationalize.io/'

#     params = {
#         'name': 'Alex'
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()

#         print(data['country'][0]['country_id'])

# except requests.exceptions.ConnectionError:
#     print('Check your internet connection')

# except requests.exceptions.ConnectTimeout:
#     print('The server does not respond')

# ==============================================================================
# Task 13. AI Request Dispatcher(POST + Headers + JSON Payload)
# ==============================================================================

try:
    url = 'https://httpbin.org/post'

    headers = {
        'Authorization': 'Bearer open-ai-mesh-2026',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': 'gpt-4o',
        'messages': [{'role': 'user', 'content': 'Optimize my Python loop'}]
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.ok:
        data = response.json()
        print(data['json'])

except requests.exceptions.ConnectionError:
    print('Check your internet connection')

except requests.exceptions.ConnectTimeout:
    print('The server does not respond')