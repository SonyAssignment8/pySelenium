#Write a program to fetch json data.
import json
with open("./demo.json") as f:
    data=json.load(f)
print(data)