# 17. Program to read a file and count occurrence of each word
f1 = open("fData.txt",'r')
data = f1.readlines()
count_dict = {}
count = 1
flat_list=[word for line in data for word in line.split()]
for i in flat_list:
    if i not in count_dict:
        count_dict.setdefault(i,count)
print(count_dict)


