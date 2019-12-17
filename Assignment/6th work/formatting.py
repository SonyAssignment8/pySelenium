#remove duplicates and print even numbers
l=[1,2,3,4,4,5,6,7,7]
print([r for r in l if r%2==0])

#Dictionary comprehension
Scaps=['AAA','BBB','CCC',]
Ssmall=['aaa','bbb','ccc']
dic={key:value for (key,value) in zip (Scaps,Ssmall)}
print(dic)
#Dictionary
s='bangalore'
str=[str for str in s[ : :-1]]
print(str)
