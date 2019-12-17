#sort ascending order and store in another variable
print("sort ascending order and store in another variable")
l=[32,4,5,1,6]
for i in range(0,5):
    print(l[i])
l.sort()
a=l.copy()
print(a)
print("========Remove duplicates========")
#Remove duplicates
li=[1,2,3,4,1,2,1,2]
s=set(li)
print(s)
# l2=[]
# print(li)
# for i in range(0,8):
#     if (li.count(li[i]))==1:
#         l2.insert(i,li[i])
# print(l2)

#take input from user and print thr sum
num=int(input("enter how many numbers you want:"))
sum=0
for i in range(0,num):
    n=int(input("enter number:"))
    sum=sum+n
print("the sum of number is:",sum)

#count upper,lowercase,special char
s='abGH$@dHy=12345'
ucount=0
lcount=0
dcount=0
scount=0
#count uppercase
for i in range(0,15):
    if(s[i].isupper()):
        ucount=ucount+1
#count lowercse
    elif(s[i].islower()):
        lcount+=1
#count digits
    elif(s[i].isdigit()):
        dcount+=1
#count specialchar
    else:
        scount+=1
print("special charecter count",scount)
print("uppercase count",ucount)
print("digit count",dcount)
print("lowerrcase count",lcount)

#get list and find sum
list=[]
sum=0
number=int(input("enter how many numbers y want:"))
for i in range(0,number):
    num=input("enter number:")
    list.insert(i,num)
for j in list:
    sum=sum+int(j)
print(list)
print(sum)

