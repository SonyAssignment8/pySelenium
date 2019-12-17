# Ques-12,13,35: largest, 2nd largest number and minimum number in list
size = int(input("Enter size for list:"))
l1 = []
for i in range(0, size):
    a = int(input("Enter elements for the list:"))
    l1.append(a)
print(l1)
l1.sort()
print('The largest or maximum value in the given list is:', l1[size - 1])
print('The 2nd largest value in the given list is:', l1[size - 2])
print('Minimum value in the given list is: ', l1[0])
