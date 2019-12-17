# to get authorization from specified API
import requests
import json
r = requests.get("http://httpbin.org/basic-auth/abcd/124",auth=('abcd','124'))
print(r.status_code)
print(r.text)