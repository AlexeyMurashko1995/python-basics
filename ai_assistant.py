import requests
import os
from dotenv import load_dotenv

try:
    load_dotenv()

    TOKEN = os.getenv('GROQ_KEY')

    api_url = 'https://api.groq.com/openai/v1/chat/completions'

    headers = {'Authorization': f'Bearer {TOKEN}'}

    prompt = input()

    payload = {
        'model': 'llama-3.1-8b-instant',
        'messages': [{'role': 'user', 'content': prompt}]
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.ok:
        data = response.json()
        print('Answer:')
        print(data['choices'][0]['message']['content'])
    else:
        print(response.text)

except requests.exceptions.ConnectionError:
    print('Check your internet connection')

except requests.exceptions.ConnectTimeout:
    print('The server does not respond')