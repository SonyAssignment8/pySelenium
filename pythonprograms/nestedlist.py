l=[1,2,['hi','hello',3,6.2],3,6]
print(l[2][0][1])

l[2].insert(0,'bye')
print(l)

d={'a':{'a1':'apple','a2':'ant'},'b':'bat'}
print(d['a'])
print(d['a']['a1'][0])