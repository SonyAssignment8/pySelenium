# we can do like this:

def fibo(p):
   if p==1:
       return 0
   if p==2:
       return 1
   return fibo(p-1)+fibo(p-2)

print(fibo(9))



