f=open("file.txt","r")
data=f.read()
s=data.split()
print(data)
print("==========================")
for i in s[::-1]:
    print(i,end=" ")
    print()
# list=[]
# for i in range(0,len(list)):
#     data=f.readlines(4)
#     for j in data:
#         list.append(j)
#         print(j[::-1])
#
#
# print(list)
# list.reverse()
# print(list)

