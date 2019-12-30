#
s="hi hello hi bye good morning hello"
string=s.split(" ")
dict={}
count=0
for i in string:
    if dict.__contains__(i):
        p=dict.pop(i)
        dict.setdefault(i,p+1)
    else:
        dict.setdefault(i,1)
print(dict)

#print 88
s2='ahbcgfghd80ghgh8'
s3=''
for i in s2:
    if i is '8':
        s3=s3+i
di={}
di.update({1:'hj',2:'hgh',3:dict})
print(di)



print(s3)