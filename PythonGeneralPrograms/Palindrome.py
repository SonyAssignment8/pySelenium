#question no 4)Given string is pallindrome
str="java"
pal=""
for i in str:
    pal=i+pal
print(pal)
if pal == str:
    print("String is palindrome")
else:
    print("String is not pallindrome")


#question no 5)check weather the given string is in upper or lower case
# strn="APPLE"
# if strn.isupper():
#     print("given string is upper case")
# else:
#     print("given string is not upper case")