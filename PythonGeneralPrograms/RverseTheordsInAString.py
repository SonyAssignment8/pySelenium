f=open("assfile.txt","r")
str=f.read()
s=str.split()
for i in s[::-1]:
    print(i,end=" ")


