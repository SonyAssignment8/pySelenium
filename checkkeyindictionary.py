dic={'k1':"Key1",'k2':"key2",'k3':"key3"}
print(dic.keys())
n=input("Enter key")
for i in dic.keys():
    if i in dic.keys():
        print("the key is ---",n,"-------The value for that key is----",dic.get(n))
        break
    else:
        print("Key does Not exists")

