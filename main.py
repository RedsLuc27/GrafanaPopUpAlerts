from dotenv import load_dotenv
import os
import requests
import json
import time
from tkinter import *
from tkinter.ttk import *

# variable def
foldernb = 0
rulesnb = 0
rulesfiring = []
rulesresolutions = []

master = Tk()

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

def inresolutions(x):
    rulesresolutions.append(x)
    master.withdraw()



# Analyze the json
while True: #Yes a while true </3
    data, r = ask()
    data = r["data"]
    groups  = data["groups"]
    for folder in groups:
        foldernb += 1
        for rules in folder["rules"]:
            rulename = rules["name"]
            rulestate = rules["state"]
            if rulestate == "firing":
                print("Firing")
                rulesfiring.append(rulename)
                if rulename not in rulesresolutions:
                    master.title("ALERT!!")
                    master.geometry("400x100")  
                    Label(master, text="The rule: " + rulename + " is firing!!").pack(pady=20)
                    inr = Button(master, text="Mark as you are actually trying to resolve it", command=lambda: inresolutions(rulename))
                    inr.pack()
                    master.update()
            rulesnb += 1
    print("Hi!")
    time.sleep(30)
