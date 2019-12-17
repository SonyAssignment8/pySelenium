#find largest number in the list
list=[]
num=int(input('enter the number of elements'))
for i in range(0,num):
    elemnets=int(input('enter the number'))
    list.append(elemnets)
    list.sort()
print('largest number in the list is:',list[-1])

