import requests
import json
r=requests.get("http://httpbin.org/basic-auth/cathi/testing",auth=('cathi','testing'))
print(r.status_code)
print(r.text)