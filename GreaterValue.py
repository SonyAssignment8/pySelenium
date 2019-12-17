a =int(input("Enter the value: A--->"))
b=int(input("Enter the value: B--->"))
c=int(input("Enter the value: C--->"))
if(a>b and a>c):
    print("A is greater")
elif(b>c and b>a):
    print("B is greater")
else:
    print("C is greater")