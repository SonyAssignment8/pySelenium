from PythonGeneralPrograms.CustomisedException import InvalidAgeError
b=12
assert b!=12,"false"
print("true")

a=int(input("enter numarator"))
b=int(input("enter denominator"))
try:
    c=a/b
    print("result",c)
except:
    print("denominator cannot be zero")
finally:
    print("exception will execute even though exception occurs")

# if 1000<=100:
#     print("true")
# else:
#