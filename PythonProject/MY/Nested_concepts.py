# nested list
l = [1, 3, 4, ['hi', 'hello', 2.4, 3], 8, 9]
for i in range(0,len(l)):
    print(l[i])
print(l[3][0][1])
l[3].append(90)
print(l)
l[3].insert(3, 'Gud morning')
print(l)

# nested dictionary
d = {'a':{'a1':'apple', 'a2':'banana'}}
print(d['a']['a2'])
print(d['a']['a1'][0])
print(d['a']['a2'][0])
d.setdefault('b','mango')
print(d)
#d.setdefault(d[a])

# nested function
def f1():
    def inner(a,b):
        print('sum:', a+b)
        print("Average:", (a+b)/2)
        print()
    inner(1,2)
    inner(12,34)
    inner(23,45)
    inner(123,456)
f1()
