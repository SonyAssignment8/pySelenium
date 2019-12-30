# function  
def commonmember(a, b):
    set1 = set(a)
    set2 = set(b)

    if len(set1.intersection(set2)) > 0:   # check length
        return (set1.intersection(set2))
    else:
        return ("no common elements")

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(commonmember(a, b))    # print common memeber for set a and set b

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(commonmember(a, b))     # print common memeber for set a and set b
