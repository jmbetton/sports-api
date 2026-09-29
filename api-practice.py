import os

import requests
from dotenv import load_dotenv

load_dotenv() # reads .env into environment variables

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise RuntimeError("API Key not set")


# Requesting Soccer Data
url = "https://v3.football.api-sports.io/leagues"

payload = {}
headers = {
    "x-apisports-key": API_KEY,
}

response = requests.request("Get", url, headers= headers, data= payload)