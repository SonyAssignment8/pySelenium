# str="himalaya"
# d={}
# for i in str:
#     d.setdefault(i,str.count(i))
#
# print("occurrance of each character is",d)
#
# str1="hi hello how hello are hi"
# d1={}
# st=str1.split()
# for i in st:
#     d1.setdefault(i,st.count(i))
# print(d1)

lst=['1','2','4','2','4','3']
di={}
for i in lst:
    if di.__contains__(i):
        c=di.pop(i)
        di.setdefault(i,c+1)
    else:
        di.setdefault(i,1)

print(di)

