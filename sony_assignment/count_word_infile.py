f=open("f2.txt",'r')
data=f.read().split()
sdtat=set(data)
for i in sdtat:
    print(i,data.count(i))
