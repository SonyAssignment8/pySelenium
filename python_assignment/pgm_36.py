# 37. Write a code to reverse a string.

s="this is joy life"
print(s)
str = ""
for i in s:
    str = i + str
print(str)

# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
#
#
# print("The original string  is : ", end="")
# print(s)
#
# print("The reversed string(using recursion) is : ", end="")
# print(reverse(s))