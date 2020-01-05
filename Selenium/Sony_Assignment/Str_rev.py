# 1.Program to reverse a string without using list or concat
s = input("Enter a string to reverse:")
rev = ''
for i in s:
    rev = i + rev
print("Reverse of given string is:", rev)


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = input("Enter a string to reverse:")
reverse(s)
