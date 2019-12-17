
#check list have even number and odd number
lst=[2,1,3,5,6,7,3,9]
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("These is even numbers",even)
print("These is odd numbers",odd)