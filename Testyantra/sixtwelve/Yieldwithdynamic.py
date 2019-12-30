def fact(n):
    f=1
    for i in range (1, n+1):
        f=f*i
        yield f

n = int(input("Enter the factorial number: "))
for i in fact(n):
    print(i)

# or we can do like
# for i in fact(n) :
# print(i)