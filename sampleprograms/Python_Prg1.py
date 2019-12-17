#declaration and initialisation of string variable
s="hello world"

#declaration and initialisation of integer variable
i=10

#declaration and initialisation of float variable
f=10.23

#declaration and initialisation of boolean variable
b=True

#declaration and initialisation of complex variable
c=10+2j

#print all variables
print("the value of s=",s,",i=",i,",f=",f,",b=",b,",c=",c)

#convert string to uppercase
print("convert string to uppercase==>",s.upper())

#convert string to lowercase
print("convert string to lowercase==>",s.lower())

#check the string is in upper or lower case
print(s.isupper())
print(s.islower())

#check the string is ends with a or not
print(s.endswith('a'))


#check the string contains only alphabet or not
print(s.isalpha())

#check the variable contanis digits ir not
print(s.isdigit())

#converts first letter to capital
print(s.capitalize())

#converts first letter of every word to capital
print(s.title())

#checks the string starts with given letter or not
print(s.startswith('w',0,6))

#checks the string ends with given letter or not
print(s.endswith('d'))

#checks the variables contains alphanumeric or not
print(s.isalnum())

#checks the given variable is numeric or not==it returns true or false
print(s.isnumeric())

#prints all the content of array string
print("The content of variable s is")
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

