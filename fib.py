#fibonacci of number using recursion
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
def series(n):
    i=1
    while i<n:
        print(fib(i),end=" ")
        i+=1
series(5)