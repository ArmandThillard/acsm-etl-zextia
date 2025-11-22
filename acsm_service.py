import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

api_url = os.getenv('API_URL')
download_url = os.getenv('DOWNLOAD_URL')
server = '?server=' + str(os.getenv('SERVER'))

def get_live_timings():
    response = requests.get(api_url)
    return response.json()

def get_results_list():
    response = requests.get(api_url + '/results/list.json' + server)
    return response.json()
    
def get_result(results_json_url):
    response = requests.get(download_url + results_json_url)
    return response.json()