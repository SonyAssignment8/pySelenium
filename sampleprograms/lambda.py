# def even(l):
#     for i in l:
#         if i%2==0:
#             print("it is even number")
#         else:
#             print("it is odd")
z=lambda i:print(i," its even") if i%2==0 else print(i," is odd")
# l=[1,2,3,4,5]
#input it may be list,set or tuple
list(map(z,{2,1,2,3,4,5}))
# even

#list comprehenssion
print([print("its even",i) for i in range(0,10) if i%2==0])