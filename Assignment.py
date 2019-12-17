#get the values from the user
a=int(input('Enter the value of A'))
b=int(input('Enter the value of B'))
#Assignment operator
a+=1
print(a)

a-=1
print(a)

a*=2
print(a)

a/=2
print(a)

b%=2
print(b)
#check the condition
if a==b:
    print("Equals")
else:
    print('Not equal')

if a!=b:
    print('Not equal')
else:
    print('Equal')


if a<=b :
    print('A is lesser than or equal to B')
else:
    print('A is greater than B ')

if a>=b:
    print('A is greater than or equal to B')
else:
    print('B is greater than A')
