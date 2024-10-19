import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

api_url = os.getenv('API_URL') + '?server=' + str(os.getenv('SERVER'))

def get_live_timings():
    response = requests.get(api_url)
    return response.json()