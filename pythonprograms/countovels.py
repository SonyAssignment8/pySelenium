# ovels='aeiou'
# str='hihello'
# ocount=0
# ccount=0
# for i in str:
#     if i in ovels:
#         ocount+=1
#     else:
#         ccount+=1
#
# print("ovels are:",ocount)
# print("continents are:",ccount)

#reverse string without using slicing
s='hello'
l=list(s)
l.reverse()
for i in l:
    print(i,end="")
s1={1,2,3,4,5}
s2={6,5,4,7,8}
s3=s1.intersection(s2)
s4=s1.difference(s2)
s5=s1.difference_update(s2)
s6=s1.intersection_update(s2)
s7=s1.union(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)