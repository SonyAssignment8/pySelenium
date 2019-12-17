class AgeInvalidError(Exception):
    pass
age = int(input("Enter Age"))
try:
    if age>=18:
        print("Valid age")
    else:
        raise AgeInvalidError
except AgeInvalidError :
    print("Enter the valid age once again return the program")
