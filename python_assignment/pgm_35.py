# 36. Write a code to count digits from a given number
n=input("enter a digit")
c=0
if n.isdigit():
    for i in n:
        c+=1
else:
    print("not number")
print("no of digits",c)
