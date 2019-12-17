f=open("hello.txt",'w')
f.write("python")


#copy abc file into hello
f=open("abc.txt","r")
lines=f.readlines()
print(lines)

for i in f:
    f1 = open("hello.txt", "a")
    f1.write(lines[i])
