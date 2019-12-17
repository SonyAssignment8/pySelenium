#check if the given string is anagram or not
s1=input('Enter the string one')
s2=input('Enter the string two')
if sorted(s1)==sorted(s2):
    print('The given string is anagram')
else:
    print('The given string is not a anagram')