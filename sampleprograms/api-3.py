import requests
import json
parm={"username":"corey","password":"testing"}
r=requests.post("http://httpbin.org/post",data=parm)
print(r.status_code)
print(r.text)