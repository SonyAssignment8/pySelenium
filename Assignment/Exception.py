a=int(input('Enter the value of a'))
b=int(input('Enter the value of b'))
try:
    c=a/b
    print('The division of a={0} and b={1}'.format(a,b),c)
except Exception:
    print('Denomination should not be Zero')

