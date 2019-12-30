# def get_input():
#     try:
#         a=int(input("enter the value"))
#         b = a-int(input("enter the value"))
#         return a,b
#     except ValueError as e:
#         print(e)
#         return get_input()
# def div(a,b):
#     try:
#         c=a/b
#         return c
#     except Exception as e:
#         print(e)
#
# def main():
#     a,b=get_input()
#     c=div(a,b)
#     print(c)
#
# main()

# # note if finally block contains return statement then the value in the finally block ill be get overided present in the buffered memoy
# def sample():
#     try:
#         return 10
#     except:
#         return 20
#     finally:
#         return 30
#
# print(sample())

#customised exception
# class Nameexception(Exception):
#     def __init__(self,message=None):
#         self.msg=message
#     def __str__(self):
#         return "exception is bcz of"+str(self.msg)
# raise Nameexception("hello")