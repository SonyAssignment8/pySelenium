import requests
#import jsons

param={"username":"corey","password":"testing"}
r=requests.post("http://httpbin.org/#/HTTP_Methods/get_get"\
               ,params=param)
print(r.status_code)
print(r.text)