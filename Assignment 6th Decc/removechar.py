#remove character from nth index
s=input('Enter the string')
c=input('Enter the character to be removed from the given string')
num=0
for i in range(0,len(s)):
    character=s[i]
    print(s[i])
    if character==c:
        num=s.index(character)
print('matching found for the index',num)
print(s.split(s[num]))
