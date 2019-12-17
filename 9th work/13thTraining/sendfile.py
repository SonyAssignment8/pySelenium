import requests
import json
parm={"username":"cathi","password":"testing"}
r=requests.post("http://httpbin.org/post",data=parm)
print(r.status_code)
print(r.text)