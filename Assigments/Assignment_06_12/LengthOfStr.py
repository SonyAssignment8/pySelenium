# Ques-22
s = input("Enter a string:")
count = 0
for i in s:
    count += 1
print("Length of given string is:", count)

# Ques-23(a)
words = 0
l = s.split(" ")
print("Number of words is:", len(words))

# Ques-23(b)
count = 0
for i in range(0, len(s)):
    if ord(s[i]) in range(65, 90) or ord(s[i]) in range(97, 122):
        count += 1
print("Number of characters is:", count)
