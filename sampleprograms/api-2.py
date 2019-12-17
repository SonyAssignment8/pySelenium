import requests
import json
parm={"page":2,"count":4}
r=requests.get("http://httpbin.org/get",params=parm)

#prints status code
print(r.status_code)

#prints data and class type
print(r.text,type(r.text))

#1.converts dictionary to json format
print(json.loads(r.text))

#or 2.converts dictionary to json format
print(r.json())

#print(json.dumps(r.text))
