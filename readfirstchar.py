f=open("file.txt","w")
f.write("First line\n")
f.write("second line\n")
f.write("third line\n")
f.write("towhundredandone line\n")
f.close()

f=open("file.txt","r")
for i in range(0,1):
    data=f.readlines(2)
    print(data)