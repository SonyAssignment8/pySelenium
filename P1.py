#1.WAP to display the numbers divisible by both 5 & 10 (1 to 100)
a = 1
while(a<=100):
    if a%5==0 and a%10==0:
        print("The numbers divisible by both 5 & 10 are :",a)
    a+=1
