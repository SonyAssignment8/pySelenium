
for i in range(1,5):

    for j in range(0,i+1):
        print("*", end="")
    print()

#methods
#No parameter and No return type
def m1():
    print('hi')
m1()

#With parameter and no return type
def m1(a):
    print('hello')
m1('J')

#With parameter and with return type
def m1(a):
    return 'Welcome'
print(m1(10))

#with parameter and no return type
def m1(a):
    print('Methods')
m1(10)



