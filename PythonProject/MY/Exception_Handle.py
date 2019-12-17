a = int(input("Enter a number:"))
b = int(input("enter 2nd number:"))
try:
    c = a/b
    print("The division of a={0} and b={1}".format(a,b),c)
except ZeroDivisionError:
    print("denominator should not be zero")
finally:
    print("exception handled")

# Custom or user Defined exception
class AgeInvalidError(Exception):
    pass
age = int(input("enter age"))
try:
    if age >= 18:
        print("valid")
    else:
        raise AgeInvalidError
except AgeInvalidError:
    print("Enter the valid age once again and RERUN the program")
