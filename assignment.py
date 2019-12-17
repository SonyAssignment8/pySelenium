#finding special charcters in string
print(list(filter(lambda ch:ch in '!@#$%^&*<>','HELLO# PYTHO$N')))

#convert given list of string to uppercase
print(list(map(lambda i:i.upper(),["apple","bannna","rose"])))

#filter remove duplicates from given string
print(set(filter(lambda i:i,"hello kill hidff")))

#filter perfect square between given numbers
def square(n):
    i = 1
    while (i * i <= n):

        if ((n % i == 0) and (n / i == i)):
            return True

        i = i + 1
    return False

print(list(filter(square,range(1,20))))

#factorial of numbers
def fact(n):
    if n in [0,1]:
        return 1
    return n*fact(n-1)
print(fact(5))

#fibonacci of number using recursion
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(4))

#packing
def dis(*args):
    print(args)
dis()
dis(10)
dis(10,20,30)

#unpacking
def dis(a,b,c):
    print(a,b,c)
dis(*"hai")
dis(* [11,2,33])
dis(* ('a','b','c'))
dis(*{'a':1,'b':2,'c':4}.items())

#unpacking key value pair
def sample(*a,**b):
    print(a)
    print(b)

sample()
sample(1,2,3,4,5)
sample(a=1,b=2,c=3)
sample({'a':1,'b':2,'c':3})
sample(1,4,2,3,5,a=10,b=20)