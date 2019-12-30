# List Methods
# Python has a set of built-in methods that you can use on lists.

# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print("1.", thistuple)

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print("2.",thistuple[1])

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print("3.",thistuple[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("4.", thistuple[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("5.",thistuple[-4:-1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("6",x)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print("7.",x)

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("8.", "Yes, 'apple' is in the fruits tuple")

# Tuple Length
# To determine how many items a tuple has, use the len() method:
# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print("9.", len(thistuple))

# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

# You cannot add items to a tuple:
# thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange" # This will raise an error
# print(thistuple)

# Create Tuple With One Item
# To create a tuple with only one item, you have add a comma after the item, unless Python will not-->
# recognize the variable as a tuple.
# One item tuple, remember the commma:
thistuple = ("apple",)
print("10.", type(thistuple))

# Remove Items
# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# Join Two Tuples
# To join two or more tuples you can use the + operator:
#Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
