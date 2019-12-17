import requests
import json
parm={"page":1,"count":3}
r=requests.get("http://httpbin.org/get",params=parm)
print(r.status_code)
print(r.text,type(r.text))
print(json.loads(r.text))
print(r.json())
json_data=json.loads(r.text)
print(json_data)
print(type(json_data))
print(r.json(),type(r.json))
