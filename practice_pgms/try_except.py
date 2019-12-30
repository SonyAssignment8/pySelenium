# class AgeInvaid(Exception):
#     pass
# age=int(input("enter the age"))
# try:
#     if age>=18:
#      print("valid")
#     else:
#         raise AgeInvaid
# except AgeInvaid:
#     print("invalid")

a=int(input("enter a"))
b=int(input("enter b"))
try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)