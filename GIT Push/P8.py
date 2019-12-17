#8.WAP to print all numbers in a range divisable by given numbers - read from the user & then divide
n = int(input("Enter the number:"))
for i in range(1,100):
    if(i%n==0):
        print("The numbers divisable by",n,"are",i)
