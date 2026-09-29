import os

import requests
from dotenv import load_dotenv

# Brief module for checking current request status and current API usage

load_dotenv() # reads .env into environment variables

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise RuntimeError("API Key not set")

url = "https://v3.football.api-sports.io/status"

payload = {}
headers = {
    "x-apisports-key": API_KEY,
}

response = requests.request("Get", url, headers= headers, data= payload)

data = response.json() # parse into python dictionary
print(data)