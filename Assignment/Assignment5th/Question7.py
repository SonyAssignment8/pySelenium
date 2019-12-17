a=10
b=20
#Use temp variable to swap two numbers
temp=a
a=b
c=temp
print(temp,a,b)

#swap without using third variable
a=10
b=20
a,b=b,a
print(a,b)