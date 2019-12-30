import json

with open("D:\\New folder\\demo.json") as f:

    data = json.load(f)
# print(data["details"]["name"])
print(data["details"])