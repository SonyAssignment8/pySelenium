print("Prime number")
print("--------------")
num = int(input("Enter the number"))
if num > 1:
    for i in range(2,num):
        if (num%i) == 0:
            print(num,"Number is not prime")
            print(i,"times",num)
            break
        else:
            print(num,"is a prime")
