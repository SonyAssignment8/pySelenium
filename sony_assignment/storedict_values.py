dic={'a':'hi','b':'hello','c':'bye'}
v=dic.values()
s=''
for i in v:
    s=s+' '+i
print(s)
f=open("f2.txt",'a')
f.write(s)
f.close()