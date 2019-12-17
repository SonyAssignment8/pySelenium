#1==>read data from file and print 7 lines
f=open("abc.txt","r")
for i in range(0,7):
    data=f.readline()
    print(data)
f.close()

#2==>given char or string is lowercase or not
string=input("enter char or string u want to enter:")
if(string.islower()):
    print("its lower")
else:
    print("its not in lowercasre")

#3==>REVERSE NUMBER USING WHILE LOOp
n=int(input("enter number:"))
rev=0
while (n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse is:",rev)

#4==>swap 2 numbers
n1=input("enter first num")
n2=input("enter second num")
print("before swapping a & b:",n1,n2)
temp=n1
n1=n2
n2=temp
print("after swapping a & b:",n1,n2)

#without using temp
a=int(input("enter first num"))
b=int(input("enter second num"))
print("before swapping a & b:",a,b)
a=a+b
b=a-b
a=a-b
print("after swapping a & b:",a,b)

#or using string formatting
print("before swapping a={0} & b={1}".format(a,b))
print("after swapping a={0} & b={1}".format(b,a))

#5==>number is even or not

number=int(input("enter number:"))
if(number%2==0):
    print("its even")
else:
    print("its odd")

#6==>get a list of number and split into even and odd
even=[]
odd=[]
count=int(input("enter how many number you want to enter"))
for i in range(count):
   no=int(input("enter number:"))
   if no%2==0:
       even.append(no)
   else:
       odd.append(no)
print("even numbers are:",even)
print("odd numbers are:",odd)

#7==>find length of string and reverse,display many times
s='Hell world'
print("length of string is:",s.__len__())
str=s[::-1]
print("reverse of string is:",str)
times=int(input("enter how many times u want to display:"))
for i in range(times):
    print(s)
