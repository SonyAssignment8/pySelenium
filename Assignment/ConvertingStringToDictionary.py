str="hi hello how are you"
s=str.split(" ")
d={}
j=0
for i in s:
    d.setdefault(s.index(i),s[j])
    j+=1
print(d)