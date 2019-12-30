l=[1,2,2,3,1,4,2]
dict={}
count=0
for i in l:
    if dict.__contains__(i):
        d=dict.pop(i)
        dict.setdefault(i,d+1)
    else:
        dict.setdefault(i,1)
print(dict)