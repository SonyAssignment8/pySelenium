import json
f = open("reva.txt","r")
data = f.read()
print(json.loads(data))
f.close()