class AgeInvalid(Exception):
    pass
age=int(input('Enter age'))
try:
    if age>18:
        print('valid')
    else:
        raise AgeInvalid
except AgeInvalid:
    print('Enter valid age')