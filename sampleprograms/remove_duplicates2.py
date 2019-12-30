# #find occurence of num in list
# l=[2,1,3,6,3,2,3,1]
# dict={}
# for i in l:
#     if dict.__contains__(i):
#         v=dict.pop(i)
#         dict.setdefault(i,v+1)
#     else:
#         dict.setdefault(i,1)
# print(dict)
#
# #occurence of char  in string
# s='aabbcchh'
# dict2={}
# for j in s:
#     if dict2.__contains__(j):
#         c=dict2.pop(j)
#         dict2.setdefault(j,c+1)
#     else:
#         dict2.setdefault(j,1)
# print(dict2)

#print only numbers in string
s2='ghh80kllk8'
s3=''
for k in s2:
    if k.isdigit():
        s3=s3+k
print(s3)