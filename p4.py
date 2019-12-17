import requests
import jsons
parm={"page":2,"count":4}

r=requests.get("http://httpbin.org/#/HTTP_Methods/get_get"\
               ,params=parm)
print(r.status_code)
print(r.text,type(r.text))
print(json.loads(r.text))
#print(json_data)
#print(type(json_data))
print(r.json())