import json
# f=open("jasonfile_data.txt","w")
# data={'a':'apple','b':"mango",'c':'orange'}
# data=(1,2,4,5)
# json_dump=json.dumps(data)
# f.write(json_dump)
# print("written successfully")
# f.close()

f=open("jasonfile_data.txt","r")
data=f.read()
print(json.loads(data))
