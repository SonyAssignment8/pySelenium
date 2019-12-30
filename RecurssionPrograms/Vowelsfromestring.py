print(list(filter(lambda ch:ch in "aeiouAEIOU","Hi hello how are youA")))
def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(len(list(filter(i for i in range(50,150) if prime(i)))))