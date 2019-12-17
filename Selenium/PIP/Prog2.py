import requests
import json
param = {"page":2,"count":4}
r = requests.get("https://httpbin.org/get",params = param)
print(r.status_code)
print(r.text, type(r.text))
print(r.json())
print(type(r.json))
