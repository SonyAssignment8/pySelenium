#Write a program to print Fibonacci series
def Fibonnacci():
    a=0
    b=1
    print(a)
    print(b)
    for i in range (10):
        c=a+b
        a=b
        b=c
        c=b
        print(c)
Fibonnacci()
