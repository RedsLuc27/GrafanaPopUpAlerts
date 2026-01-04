from dotenv import load_dotenv
import os
import requests
import json

# variable def
folder = 0


# load dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL_LOGIN")

# ask the API
response = requests.get(url + "/api/prometheus/grafana/api/v1/rules")
data = response.json()
print(data)

#load json
r = json.loads(response.text)


# Analyze the json
data = r["data"]
groups  = data["groups"]
for i in groups:
    folder += 1


# debug
print(groups)
print(folder) 