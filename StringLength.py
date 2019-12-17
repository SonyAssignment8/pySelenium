# Python program to demonstrate the use of
# len() method

# Length of below string is 5
string = "geeks"
print(len(string))

# Length of below string is 15
string = "geeks for geeks"
print(len(string))
# or
string = input("Enter the string for length: ")
print(len(string))
print(string)

# reverse the string
# str = "Python"            # initial string
str1 = input("enter string for reverse :")
reversedString = []
index = len(str1)          # calculate length of string and save in index
while index > 0:
    reversedString += str1[index - 1]    # save the value of str[index-1] in reverseString
    index = index - 1                   # decrement index
print(reversedString)                   # reversed string

# Print string multiple times
str3 = input("enter the string for print multiple times: ")
print(str3 * 3)
