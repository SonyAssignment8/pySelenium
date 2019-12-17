# to calculate the average of a numbers in given list
n = int(input("Enter the number of elements to be inserted:"))
a=[]
for i in range(0,n):
    elem=int(input("Enter element:"))
    a.append(elem)
    avg=sum(a)/n
    print("Average of elements in list is:",round(avg,2))