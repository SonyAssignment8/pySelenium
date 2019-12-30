#swap two numbers
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#swap two numbers using temp variable
a=10
b=20
temp=0
temp=a
a=b
b=temp
print(a)
print(b)

#program to check the given number is even or not
num=9
if num%2==0:
    print("given number is even")
else:
    print("given number is odd")