# Ques-19 Anagram
s1 = input("Enter first string:")
s2 = input("Enter second string:")
if sorted(s1) == sorted(s2):
    print("Given strings are anagram")
else:
    print("Given strings are not anagram")

# Ques-20 Counting vowels in a given string
strng1 = input("Enter a string to count vowels:")
count = 0
for i in range(0, strng1.__len__()):
    if strng1[i] in ['a', 'i', 'e', 'o', 'u']:
        count += 1
print("Number of vowels in the given string is:", count)

file = open("abc.txt", 'w')
file.write("Assuming that the first element in the list has the longest length")

# Ques-21
file = open("abc.txt", 'r')
fData = file.readlines()
s = fData[0]
print("Updated file with blank space replaced with hyphen is:", s.replace(" ", "-"))
file.close()

# Ques-24 Creating new string from two given strings(by first two and last two characters of string 1 and 2
# respectively)
s1 = input("Enter a first string:")
s2 = input("Enter a second string:")
s3 = s1[0:2] + s2[-2:]
print("The new string is :", s3)

# Ques-28,29,30: Displaying common and uncommon characters in the two given strings
s1 = set(input("Enter a first string:"))
s2 = set(input("Enter a second string:"))

for i in s1:
    if i in s2:
        print("common character:", i)
    elif i not in s2:
        print("uncommon character from s1:", i)

# Ques-31 letters not present in both the string
s1 = (input("Enter a first string:"))
s2 = (input("Enter a second string:"))
s3 = s1 + s2
s4 = set(s3.lower())
s = []
for i in range(97, 123):
    if chr(i) not in s4:
        s.append(chr(i))
print("Uncommon characters in both the string is:", s)
