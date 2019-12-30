# def prime(n):
#     if n==1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# bool=prime(4)
# if bool==False:
#     print("its not prime")
# else:
#     print("its prime")
#print(list(filter((lambda i,n:print(" its not prime") if n%i==0 else print(' its prime')),range(2,6))))
# #nums = range(2, 50)
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, range(2,9))
print (list(nums))
