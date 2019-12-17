f=open("file.txt","r")
data=f.read()
f.close()
d=""
count=1
for i in data:
    for j in i:
        print(j.split(" "),end="")

    #print(i,end="")




print("Total charactors present in the file is ",data.__len__())
print(count)

