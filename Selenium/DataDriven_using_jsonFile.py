import json

with open(".\my_jason.json") as f:
    data = json.load(f)
    print(data["details"]["name"])
    print(data["details"]["class"])

with open("C:\\Users\\Jyoti\\Desktop\\mmm.json") as f:
    data = json.load(f)
    print(data["details"]["name"])
