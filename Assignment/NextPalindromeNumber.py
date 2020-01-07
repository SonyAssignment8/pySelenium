#find the next palindrome number
def reverse(n):
    reverse=0
    while n>0:
        r=n%10
        n=n//10
        reverse=reverse*10+r
        return reverse
