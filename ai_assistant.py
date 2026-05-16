import requests
import os
from dotenv import load_dotenv

load_dotenv()

# TOKEN = os.getenv('HF_TOKEN')

api_url = 'https://text.pollinations.ai/'

headers = {
}

payload = {
    'messages': [{'role': 'user', 'content': 'Tell me a short joke about Python coding'}]
}

response = requests.post(api_url, headers=headers, json=payload)

print(response.text)
print(response.status_code)
