from re import split

str = 'My Name is Jyoti sahu and birthdate is 08-02-1992!!'
Ucase = 0
Lcase = 0
digit = 0
spChar = 0
for i in range(0,len(str)):

    if ord(str[i]) >= 48 and ord(str[i]) <= 57:
        digit +=1
    elif ord(str[i])>=65 and ord(str[i])<=90:
        Ucase += 1
    elif ord(str[i])>=97 and ord(str[i])<=122:
        Lcase +=1
    else:
        spChar+=1
print('Number of digits in given string is:', digit)
print('Number of UpperCase characters in given string is:', Ucase)
print('Number of LowerCase characters in given string is:', Lcase)
print('Number of Special characters in given string is:', spChar)

