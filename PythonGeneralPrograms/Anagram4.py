# @ 21)check weather the given number is anagram or not
str1 = 'TAB'
str2 = 'BAT'
a = False
for i in str1:
    if str2.__contains__(i):
        a = True
    else:
        a = False
if a == True:
    print("two string are anagram")
else:
    print("two strings are not anagram")
