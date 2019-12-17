# def add(sal):
#     return sal+10/100*sal

#salary increment by 10%
add=lambda sal:sal+10/100*sal
print(list(map(add,[1000,2000,3000])))
#even numbers
print(list(filter(lambda n:n%2==0,[11,22,33,44])))

#prime number
def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print([i for i in range(50,100) if isprime(i)])
#finding vowels in string
print(list(filter(lambda ch:ch in 'aeiouAEIUO','HELLO PYTHON')))

#check string is in a-z and A-Z
print(list(filter(lambda ch:ch>='a' and ch<='z'or ch>='A' and ch<='Z' ,'123ASD')))

