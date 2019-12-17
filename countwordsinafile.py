f=open("file.txt","w")
f.write("Hello world\n")
f.write("First letter\n")
f.close()

f=open("file.txt","r")
data=f.read()
d=data.split(" ")
# d=d[::-1]
# j="".join(d)
print(data[::-1])
print(d)
count=0
for i in d:
    count+=1
print(count)
f.close()