#reversr a string without using list or concat
s='good morning'
s1=s[::-1]
print(s1)

#another way
s2=''
for i in s:
    s2=i+s2
print(s2)