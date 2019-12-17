class AgeInvalidError(Exception):
    pass
#raise custom exception
age=int(input("enter your age:"))
try:
    if age>=18:
        print("valid age")
    else:
        raise AgeInvalidError
except  AgeInvalidError:
    print("invalid age")
finally:
    print("finally")

#dividsion by zero error
a=int(input("enter a value:"))
b=int(input("enter b value:"))
try:
    c=a/b
    print('the division of a={0} and '
          'b={1}'.format(a,b),c)
except ZeroDivisionError:
    print("denominator shud not be zero")
finally:
    print("please enter valid number")
