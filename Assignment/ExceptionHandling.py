a=int(input('Enter a'))
b=int(input('Enter b'))
try:
    c=a/b
    print('result',c)
except ZeroDivisionError:
    print('Denominator should not be zero')
finally:
    print('Exception occur or not exceute this')
age=int(input('Enter age'))
if age>=18:
    print('valid age')
else:
    print('Invalid age')