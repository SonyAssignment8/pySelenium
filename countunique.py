def convert(list):
    return set(list)
f=open("file.txt","r")
data=f.read()
print(data)
lst=[]
lst.append(data)
print(lst)


set=convert(lst)
print(set)