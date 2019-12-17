list = []
for i in range(1,8):
     # Taking input from user
    a = int(input("Enter elements from the list:"))
    list.append(a)
print(list)
sum = 0
for i in range(0,len(list)):
    sum = sum+ list[i]
print("Sum of the elements of list:", end='')
print(sum)