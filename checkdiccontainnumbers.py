dic1={2:2,3:3,4:4}
dic2={}
for i in dic1.values():
    for j in dic1.keys():
        dic2.setdefault(j,pow(j,i))

print(dic2)