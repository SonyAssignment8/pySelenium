a=int(input("Enter numerator"))
b=int(input("Enter dreaminator"))

try :
    c=a/b
    print("Result",c)
except ZeroDivisionError :
    print("Denaminator should not be zero")
finally:
    print(" Exception are run or not in finally block")


#  Final block will be Excuted if exception block is Execuated or not
