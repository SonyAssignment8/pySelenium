# Ques-25
dctnry = {'k1': 'apple', 'k2': 'mango', 'k3': 'grapes'}
dctnry.setdefault('k4', 'guava')
print(dctnry)

# Ques-26
k = input("Enter a value for key:")
if k in dctnry.keys():
    print("Given key already exists in dictionary")
else:
    print("Given key doesn't exist, so adding it to dictionary ")
dctnry.setdefault(k, ' ')
print(dctnry)

# Ques-27
k = int(input("Enter a value for key:"))
dict2 = {}
dict2.setdefault(k,k*k)
print(dict2)


