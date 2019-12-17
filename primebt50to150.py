def isprime(n):
    if n==1:
        return False
    for i in range (2,n):
        if n%i==0:
         return False
    return True


# we do like that
print(list(filter(isprime , range(50,150))))
print((len([i for i in range(50,150) if isprime(i)])))
