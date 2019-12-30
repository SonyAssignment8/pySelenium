# List
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
list = ["Banana", "Orange", ",Apple"]
print("1.", list)

# Access Items
# You access the list items by referring to the index number:

familylist = ["apple", "banana", "cherry"]
print("2.", familylist[0])  # Print the second item of the list:

# Negative Index
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
familylist = ["apple", "banana", "cherry"]
print("3.", familylist[-2])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Return the third, fourth, and fifth item:
familylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("4.", familylist[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.
# By leaving out the start value, the range will start at the first item:

familylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("5.", familylist[4])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# Example
# This example returns the items from index -4 (included) to index -1 (excluded)
familylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("6.", familylist[-4:-1])

# Change Item Value
# To change the value of a specific item, refer to the index number:
# Example
# Change the second item:
familylist = ["apple", "banana", "cherry"]
familylist[1] = "blackcurrant"
familylist[2] = "Atul"
print("7.", familylist)

# Loop Through a List
# You can loop through the list items by using a for loop:
# Example
# Print all items in the list, one by one:
familylist = ["1.apple", "2.ba", "3.cherry"]
for x in familylist:
    print(x)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example
# Check if "apple" is present in the list:
familylist = ["apple", "ba", "cherry"]
if "apple" in familylist:
    print("Yes, 'apple' is in the fruits list")

# List Length
# To determine how many items a list has, use the len() function:
# Example
# Print the number of items in the list:
familylist = ["apple", "banana", "cherry"]
print("8.", len(familylist))

# Add Items
# To add an item to the end of the list, use the append() method:
# Example
# Using the append() method to append an item:
familylist = ["apple", "banana", "cherry"]
familylist.append("orange")
print("9.", familylist)

# To add an item at the specified index, use the insert() method:
# Insert an item as the second position:
familylist = ["apple", "banana", "cherry"]
familylist.insert(1, "orange")
print("10.", familylist)

# Remove Item
# There are several methods to remove items from a list:
# Example
# The remove() method removes the specified item:
familylist = ["apple", "banana", "cherry"]
familylist.remove("banana")
print("11.", familylist)

# The pop() method removes the specified index, (or the last item if index is not specified):
familylist = ["apple", "banana", "cherry"]
familylist.pop()
print("12", familylist)

# The del keyword removes the specified index:
familylist = ["apple", "banana", "cherry"]
del familylist[2]
print("13.", familylist)

# The del keyword can also delete the list completely:
familylist = ["apple", "banana", "cherry"]
del familylist

# The clear() method empties the list:
familylist = ["apple", "banana", "cherry"]
familylist.clear()
print("15.", familylist)

# Make a copy of a list with the copy() method:
familylist = ["apple", "banana", "cherry"]
mylist = familylist.copy()
print("16.", mylist)

# Another way to make a copy is to use the built-in method list().
# Make a copy of a list with the list() method:
#thislist = ["apple", "banana", "cherry"]
#mylist = list(thislist)
#print("17.", mylist)

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("17.", list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one:

# Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print("18.",list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("19.",list1)

familylist = ["atul", "anshul", "ranu"]
a=familylist.count(1)     # Returns the number of elements with the specified value
print(a)
# familylist.index(0)     # Returns the index of the first element with the specified value
#familylist.extend(2)    # Add the elements of a list (or any iterable), to the end of the current list
# thislist.insert("abhi")
familylist.pop()        # Removes the element at the specified position
familylist.reverse()
familylist.sort()
