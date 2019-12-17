#19.WAP to remove the nth index char from a non empty string - read value from user
def remove(string, n):
    first = string[:n]
    last = string[n + 1:]
    return first + last


string = raw_input("Enter the string:")
n = int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))