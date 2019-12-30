def palindrome(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return  rev
n=int(input("enter the number:"))
rev=palindrome(n)
if rev==n:
    print("its palindome")
else:
    while True:
        n=n+1
        if n==palindrome(n):
            print("next palindrome is:",n)
            break
