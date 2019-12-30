#yield is a key word
# num=int(input("enter the number"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     print(fact)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        yield f
n=int(input("enter the number"))
for i in fact(n):
    print(i)

