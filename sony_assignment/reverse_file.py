f=open("f1.txt","r")
l=f.readlines()
#reverse each line
for i in l:
    print(i[::-1])
#reverse lines in file
l.reverse()
for j in l:
    print(j)