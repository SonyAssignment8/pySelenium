s={4,2,1,6,7,8}
s.add(10)
print(s)
s.pop()
s1={2,1,3}
s.update(s1)
print(s)
s2=s.union(s1)
print(s2)
s3=s.difference(s1)
print(s,s1)
print(s3)
s4=s.intersection(s1)
print(s4)
for i in s:
    print(i)