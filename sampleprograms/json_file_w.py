import json
# f=open("f1.txt","w")
# data={'a':'apple','b':'bat'}
# json_data=json.dumps(data)
# f.write(json_data)
# f.close()

f=open("f1.txt",'r')
data=f.read()
print(json.loads(data))
f.close()
