num=input("Enter a number")
count=1
if num.isdigit():
   for i in num:
       count+=1
else:
    print("Not numbers,Please run again")
print("No of the digits are----",count)