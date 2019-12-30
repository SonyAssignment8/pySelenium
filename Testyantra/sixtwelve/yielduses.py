def fact(n):
    f=1
    for i in range (1, n+1):
        f=f*i
        yield f

for i in fact(5):
    print(i)