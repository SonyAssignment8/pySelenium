#1.To print first char in a file
f = open("new.txt","w")
f.write("Good Morning")
f.close()

f=open("new.txt","r")
data=f.read()
print(data[0])


f.close()
