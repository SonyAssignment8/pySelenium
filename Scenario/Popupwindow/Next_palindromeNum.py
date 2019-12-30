#WAP to find the next palindrome number
n = int(input("Enter any number :- "))

reverse = 0
temp = n

while (n!=0):
    reverse = reverse * 10
    reverse = reverse + n%10
    n=n//10
if(temp==reverse):
    print ("Already palindrome:: ")

if(temp != reverse):
     new_temp = temp
     new_reverse = 0
     for i in range(new_temp,new_temp+10):
        while(temp != 0):
            new_reverse = new_reverse * 10
            new_reverse = new_reverse + temp%10
            temp = temp//10
        if(new_temp==new_reverse):
             print ("Next pallindrome is :- ",new_temp)
             break
        if(new_temp != new_reverse):
             temp = new_temp+1