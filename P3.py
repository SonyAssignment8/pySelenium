#3.To print file data in reverse order(reverse,slicing)
f = open("new2.txt","w")
f.write("Good Night")
f.close()

f=open("new2.txt","r")
data=f.read()
print(data)
print(data[::-1])
