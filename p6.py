import requests
import json

param={"username":"corey","password":"testing"}
r=requests.get("http://httpbin.org/#/Auth/get_basic_auth\abcd\124",auth=('abcd','124'))
print(r.status_code)
print(r.text)