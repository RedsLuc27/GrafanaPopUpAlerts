from dotenv import load_dotenv
import os
import requests
import json

# variable def
foldernb = 0
rulesnb = 0
rulesfiring = []
i = 0

# load dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL_LOGIN")

# ask the API
def ask():
    response = requests.get(url + "/api/prometheus/grafana/api/v1/rules")
    data = response.json()
    r = json.loads(response.text)
    return data, r


# Analyze the json
data, r = ask()
data = r["data"]
groups  = data["groups"]
for folder in groups:
    foldernb += 1
    for rules in folder["rules"]:
        rulename = rules["name"]
        rulestate = rules["state"]
        if rulestate == "firing":
            rulesfiring.append(rulename)
        rulesnb += 1
        


# debug
print(groups)
print(folder)
print(foldernb, rulesnb) 
print(rulesfiring)
