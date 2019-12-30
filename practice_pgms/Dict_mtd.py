d={1:'aaa',2:'bbb',3:'ccc',4:'ddd'}
print(d.keys())
print(d.values())
d.update({5:'ddd',6:'eee'})
print(d)
print(d.pop(5))
d.setdefault(7)
d.setdefault(0,'ggg')
print(d.items())
#dict.fromkeys(keys, value)
k=('x1','x2','x3')
v=(3,3)
d1=d.fromkeys(k,v)
print(d1)
print(d.get(4))
print(d.popitem())

for i,j in d.copy().items():
    print(i,j)