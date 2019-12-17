#10.WAP to get list of numbers & split them into even & odd
list = [2,1,2,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers are:",even)
print("odd numbers are:",odd)