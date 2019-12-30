# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781
# print(phonebook)

# or
# phonebook = {
#    "John": 938477566,
#    "Jack": 938377264,
#    "Jill": 947662781
#}
# print(phonebook)

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of
# the values stored in it. To iterate over key value pairs, use the following syntax
phonebook = {"john": 9809876543, "jack": 9876543265, "jill": 8907654326}
for name,number in phonebook.items():
    print("phone no of %s is %d" % (name,number))

print("------------------------------------------------------------------------------------")
# Removing a value
# To remove a specified index, use either one of the following notations:
del phonebook["john"]
print(phonebook)

# or we can do like this :
phonebook.pop("jack")
print(phonebook)



