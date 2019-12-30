# #13)find largest number in list
# l1=[24,56,2,45,80,60]
# l1.sort()
# print("largest number of the list is",l1[-1])
#
# # Q 14)
# print("Second biggest number is ",l1[-2])
#
# # Q 15) merge two list and sort
# l2=[89,90,23,4,45,63]
# l2.extend(l1)
# l2.sort()
# print("sorted the merged list in ascending order",l2)
# print("sorted the merged list in descending order ",l2[::-1])

#q no 18) WAP to generate random numbers and append them to list
# import random
# lst=[]
# for i in range(1,10):
#     lst.append(random.randint(1,10))
# print(lst)
#
# # Q 19)WAP to swap 1st last values of list
# swp=[20,45,67,89,21,24,80]
# print("list before swapping",swp)
# swp[0],swp[-1]=swp[-1],swp[0]
# print("list after swapping 1st and last ",swp)

#WAP to print table
# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n*i,end=" ")

#Read Data i,e tyss from user it should accept 3 times if correct give result otherwise throw invalid message

class InvalidPasswordError(Exception):
    pass


count=0
while count<=2:
    data = input("enter the data")
    try:
        if data=="tyss":
            print("input acepted")
        else:
            raise InvalidPasswordError

    except InvalidPasswordError:
        print("Invalid password")
        count+=1




