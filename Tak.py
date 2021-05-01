import json


data = list()
with open("7.json", "r") as tasks:
    data = json.load(tasks)

print(data)