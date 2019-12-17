a=2
b=6
# Arithmatic operator
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b//a)
print(a**b)

#Assignment operator
print(a==b)
a+=1
print("Assignment operator +=",a)
b-=1
print("Assignment operator -=",b)
a*=b
print("Assignment operator *=",a)
a/=b
print("Assignment operator /=",a)

#Relational operator
if a==b:
    print("both r equal")
else:
    print("not equal")
if a>=b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("both r equal")

#Membership operator
l=[1,2,3,4,5,5.67]
if(0 in l):
    print("it is present")
elif(0 not in l):
    print("it is not present")

#Identity operator
d=[1,2,3]
b=d
if(b is d):
    print("both r same")
else:
    print("both r not equal")

#for loop
for i in l:
    print("the value of i is:",i)

 #range method
for i in range(5,15,2):
    print(i,end=" ")

print("-----------")
for i in range(10):
    print(i,end=" ")
print("-------------")
for i in range(1,10,2):
    print(i)

#while loop
print("------------")
q=10
while q<=15:
    print(q)
    q+=1

print("-------------")
#break
for i in range(10):
    print(i)
    if(i==3):
        break
print("--------------")
for i in range(10):
    if i%2==0:
        continue
    print(i)
print("=================palindrome==========")
s="rar"
rev=s[::-1]
print("the reverse is=",rev)
def palindrome(rev):
    if rev==s:
        print("its palindrome")
    else:
        print("not palindrome")

palindrome(rev)
