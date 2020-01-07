#Program to reverse a string without using list or concat
def reverse(string):
    string = "".join(reversed(string))
    return string


s = "Welcome to Python"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using reversed) is : ", end="")
print(reverse(s))

#Or this code

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "hello world"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

