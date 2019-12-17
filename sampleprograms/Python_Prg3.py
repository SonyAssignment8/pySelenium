#Replaces the old string with new string
Str="Good Morning"
print(Str.replace('Morning','Afternoon'))

'''counts the occurence of substring.
It will takes substring, starts with ,ends with index as an arguments'''
print(Str.count('hel'))

'''counts the substring  from 0 position till end,
and returns the occurence count'''
print(Str.count('hel',0))

'''counts the substring  from 0 position to 11,
and returns the occurence count'''
print(Str.count('world',0,11))

#it will returns index value of h
print(Str.find('h'))

'''it will return first occurence of index value
and start searching from 0 to till end'''
print(Str.find('d',0))
      

#it will return index value and start searching from 0 to 4
print(Str.find('d',0,4))

#it also returns index value of given stirng
print(Str.index('o'))

s1="Hello Hi"

#it will remove specified string from left side of the given string
print(s1.lstrip('H'))

#it will remove specified string from right side of the given string
print(s1.rstrip('o Hi'))

#it will split based on space
print(s1.split(' '))

s2="Hello Hi How"

#split removes and then split based on 'H'
print(s2.split('H'))

#inserts '-' after every charecter
print("-".join(s2))

# l is List

l=[1,2,'hi',4.32]
print(l)

#it will append given value to list
l.append("Are You")
print(l)

#remove last value
print(l.pop())

#insert at specified index
l.insert(0,'d')
print(l)

#it will remove specified value
l.remove('d')
print(l)

#it will return the occurence
print(l.index('hi',0))


#it will reverse the list
l.reverse()
print(l)

l1=[10,2,6,1,7,8]
li=['s','a','r','b']

#it will sort the list in ascending order
l1.sort()
print('sorted list',l1)
li.sort()
print('sorted alphabert list', li)


#copy one list to another list
a=l.copy()
print('new copied list a',a)
#it will append one list to another
l1.extend(l)
print(l1)

#Tuple is data type, it is immutable,not growable,insertion not possible
t=(1,'h',6,5.3,6)

'''it searches given value from start index to ending index
and returns index position '''
print(t.index(6,0,3))
print(t)

#it will count the number of times the given value present
print(t.count(6))
print(t.count(5.3))
s=" hello hi " 
print(s.strip())

#set
s={1,2,'hi','good',20.36}

#it will specify the type of object
print(type(s))
print(type(l))

#it will give the address of element
print(id(s))

#Dictionary
d={'a1':'client1','a2':'client2','a3':'client3'}
print(d)

#prints all the keys
print(d.keys())

#returns all values
print(d.values())

#returns value of key
print(d.get('a1'))

#deletes the specified key
print(d.pop('a1'))
print(d)

#reinitialise the key value
print(d.setdefault('a4','client5'))
d['a5']='client6'
print(d)

     
