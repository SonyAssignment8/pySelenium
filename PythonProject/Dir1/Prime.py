class P_Num():
    num = int(input("Enter a number to print prime number till a range:"))
    c = 0
    if num > 1:
        for i in range(2,num):
         if(num%i)==0:
            break
         else:
            print(num)




