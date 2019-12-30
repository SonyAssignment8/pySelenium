#for loop for dictionary
# users={"sam":"active","ram":"inactive","dam":"active"}
# active_users={}
# for user,status in users.items():
#     if status=='inactive':
#         del users[user]
# print(users)

#print even numbers
# for i in range(2,10):
#     if i%2==0:
#         print("even number:",i)
#         continue
#     print("odd numbers are:",i)

#print inll integer in string
s="hi23 good"
# s1=''
# for i in s:
#     if i.isdigit():
#      s1=s1+i
# print(s1)

#slicing
# print(s[len(s):-1:-1])
# print(s[:-9:-1])

# li=[1,1,2,3,6,6,4,5,6,6,]
# st=list(set(li))
# #li=list(st)
# print(st)
s='HELLO'
print(s[0:3])
print(s[-4::-1])
print(s[::-3])