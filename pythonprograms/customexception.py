from pythonpgms.pythonprograms.tryexcept import AgeInvalidError
age=int(input("enter your age:"))
try:
    if age>=18:
        print("valid age")
    else:
        raise AgeInvalidError
except  AgeInvalidError:
    print("")
