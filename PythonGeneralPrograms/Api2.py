import requests
import json
parm={"hi":"hello","count":6}
r=requests.post("http://httpbin.org/post",data=parm)

#print status of the code
print(r.status_code)

#print data and class type
print(r.text,type(r.text))

#convert code from dictionary format  to json format
print(json.loads(r.text))

#convert code from dictionary to json
print(r.json())