# Ques-18
index = int(input("Enter index number to delete the character:"))
s = input("Enter a string value:")
first = s[:index]
last = s[index + 1:]
print("String value after removing the given index is:", first + last)


