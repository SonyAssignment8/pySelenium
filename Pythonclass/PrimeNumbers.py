# start=int(input("Enter the start range"))
# end=int(input("enter the end range"))
# for num in range(start,end):
#     if num>0:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)

n=3
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("its prime num")
else:
    print("not prime")



