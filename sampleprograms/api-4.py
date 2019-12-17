import requests
import json
r=requests.get("http://httpbin.org/basic-auth/aaa/123",auth=("aaa",'123'))
print(r.request)
print(r.text)