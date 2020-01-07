# Any program for list comprehension
#to find even numbers within the range
n=int(input("Enter a number to check if is prime number or not"))
def prime(n):
    print([i for i in range(1,50) if n%i==0])
prime(n)