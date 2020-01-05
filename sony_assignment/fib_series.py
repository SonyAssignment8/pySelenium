def fib(n):
   a=0
   b=0
   c=1
   for i in range(0,n):
       a=b
       b=c
       c=a+b
       print(a)

print(fib(9))