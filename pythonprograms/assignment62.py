#insert key.value to dictionary and search for key
dic={}
dic.setdefault(1,'name')
dic.setdefault(2,'age')
dic.setdefault(3,'address')
print(dic)
k=int(input("enter the key you want to search:"))
if(dic.__contains__(k)):
    print("key is present")
else:
    print("key is not present")

#generate dict in the form n:n*n
d={}
i=int(input("enter the number:"))
for j in range(1,i):
    k=j
    v=j*j
    d.setdefault(k,v)
print(d)

#find common letters in 2 input strings
s1='abcd'
s2='cdefh'
print("common letters are:")
for i in s1:
    if i in s2:
        print(i)

#display letters which r in first string not in second string
print("letters which r in first string not in second string:")
for i in s1:
    if i not in s2:
        print(i)

#display the letters not in both string
print("the letters not in both string")
s3=s1+s2
#print(set(s3))
for i in s3:
    if s3.count(i)==1:
        print(i)
#generate
#2*1=2
#2*2=4
i=2
n=int(input("how many numbers you want:"))
for j in range(1,n):
    res=i*j
    print(i,'*',j,'=',res)

#read value from user 3 times,if it is equal to tyss then ==valid else invalid

for i in range(0,3):
    str = input("enter tyss string: ")
    if str.__eq__('tyss'):
        print("valid")
        break
    else:
        print("invalid")

#find max min value in list
l=[2,6,9,1,3,4,7,10,3.2]
l.sort()
print(l)
print("max is:",max(l))
print("min is:",min(l))
