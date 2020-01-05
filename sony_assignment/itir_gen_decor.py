# #iterator
# li=['hi',2.3,54,True]
# i=iter(li)
# print(next(i))
# print(next(i))
# print(next(i))
#
# #decorator
#
# def ValidAge(func):
#     def InvalidAge():
#         age=func()
#         if age<18:
#             print("invalid age")
#         else:
#             print("valid age")
#     return InvalidAge
#
# @ValidAge
# def Age():
#     age=int(input("enter age:"))
#     return age
# Age()

#generator
def my_gen():
    n=1
    print("first")
    yield n

    n=n+1
    print("second")
    yield n

    n=n+1
    print("thrid")
    yield n

#use for loop to print
for i in my_gen():
    print(i)

#or use iterator
i=iter(my_gen())
print(next(i))