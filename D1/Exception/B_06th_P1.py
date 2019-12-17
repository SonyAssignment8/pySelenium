a = int(input("Enter a value for A:"))
b = int(input("Enter a value for B:"))
try:
    c = a/b
    print("The division of a{0} and b{1}",format(a,b),c)
except ZeroDivisionError:
    print("Denomination should not be zero")
