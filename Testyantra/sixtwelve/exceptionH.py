a=int(input("enter first number"))
b=int(input("enter first number"))

try:
    c=a/b

    print("the divisinal is ", c)

except ZeroDivisionError:
    print("Divisional is not by zero")

