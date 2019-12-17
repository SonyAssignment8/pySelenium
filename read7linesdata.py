
#to read the data use for loop
f=open("ab.txt","r")
for i in range(1,7):
    data=f.readlines(i)
    print(data)
f.close()