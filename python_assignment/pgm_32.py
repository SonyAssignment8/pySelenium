# # 33. Write a code to sort elements present in list (without using built in method)
# l1 = [999,44,22,6,2,1]
# l2 = []
#
# while l1:
#     min = l1[0]  # arbitrary number in list
#     for i in l1:
#         if i < min:
#             min = i
#     l2.append(min)
#     l1.remove(min)
#
# print(l2)

l = [64, 25, 12,888]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)