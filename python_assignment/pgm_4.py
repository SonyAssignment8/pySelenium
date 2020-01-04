# 4. Program to read a file and reverse each line
f=open("f1.txt","r")
list=[]
for i in range(0,12):
    d=f.readlines(3)
    for j in d:
        list.append(i)
        print("reverse contains of a file is: ",j[::-1])
# print(list)
# list.reverse()
# print(list)