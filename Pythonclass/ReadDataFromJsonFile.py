import json
data=json.load(open("./JsonFile.json"))
print(data["details"]["name"])