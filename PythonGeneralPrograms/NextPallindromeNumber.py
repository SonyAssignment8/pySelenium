
def reverse(n):
    reverse=0
    while n>0:
        rem=n%10
        n=n//10
        reverse=reverse*10+rem
    return reverse
n=int(input("enter the number"))
if n==reverse(n):
    print("number is already pallindrome")
else:
    while True:
        n+=1
        if n==reverse(n):
            print("Next palindrome is :",n)
            break





