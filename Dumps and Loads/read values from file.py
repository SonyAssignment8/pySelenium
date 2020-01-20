import json
f = open("reva.txt","w")
data = {'a':"apple",'b':"bat"}
json_data = json.dumps(data)
f.write(json_data)
print("Successfully Written")
f.close()