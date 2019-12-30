# question number 2) read data frm file and display in console
f=open("ReadFile.txt","r")
# data=f.read()
# print(data)

# Question num 3)read only 7 lines from file

for i in range(0,7):
    comline=f.readline()
    print(comline)

