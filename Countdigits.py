# Write a code to count digits from a given number
n=int(input("Enter a number"))
count=0
while n>0:
    n=n//10
    count+=1
print("Number of digits present in the number is:",count)
