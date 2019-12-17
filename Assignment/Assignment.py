#Question 1
#given list is
l=[1,2,3,4,1,2,1,2]
set={1,2}
#Pass the same list to set ,to remove duplicates
set.update(l)
print(set)

#Question 2
#List
l1=[3,4,5,1,6]
print('The given list l1 is:',l1)
#sort the numbers in the list
l1.sort()
print('The sorted list is of l1:',l1)
#copy the elements of the list in another variable
l2=l1.copy()
print('The contents are stored in new variable l2:',l2)

#Question 3
list=[]
for i in range (1,10):
    l=int(input('Enter the elements'))
    list.append(l)
print(list)
sum=0
for j in range (0,len(list)):
    sum=sum+list[j]
print(sum)

#Question 4
a=input('Enter the name')
d={'sujitha':'python','Divya':'python','jyoti':'python','danasekar':'Appium','nila':'Appium','susma':'Appium','susmitha':'javascript','supriya':'javascript'}
python=[]
Appium=[]
javascript=[]
for i in d:
    if a=='python':
        python.append[i[0]]
    elif a=='javascript':
        javascript.append[i[1]]
    elif a=='Appium':
        Appium.append[i[0]]
print(python)
print(Appium)
print(javascript)

#Question 5
a=input('Enter the given string')
ucount=0
lcount=0
ncount=0
count=0

for i in range (len(a)):
    if a[i].isupper():
        ucount+=1
    elif a[i].islower():
        lcount+=1
    elif a[i].isnumeric():
        ncount+=1
    else:
        count+=1
print('number of upper case is:',ucount)
print('number of lower case is:',lcount)
print('number of numbers is:',ncount)
print('number of special characters is:',count)

#Question 6
#calculate leap year
'''A year is leap year if the following conditions are satisfied:
    Year is multiple of 400.
    Year is multiple of 4 and not multiple of 100.'''

year=int(input('Enter the year'))
def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Driver Code
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")