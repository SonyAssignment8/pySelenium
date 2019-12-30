class AgeinvalidError(Exception):
    pass
age = int(input("Enter Age:"))
try:
    if age>=18:
        print("Valid age=>issue voter id")
    else:
        raise AgeinvalidError
except AgeinvalidError:
    print("Enter the valid age once again RErun the program")

