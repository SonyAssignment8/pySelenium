#count unique word in the file
count=0
f=open('f.txt','r')
data=set(f.readlines())
count=len(data)
print(count)
f.close()

