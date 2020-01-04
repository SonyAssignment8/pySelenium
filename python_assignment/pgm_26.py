# 27. Write a program for custom iterator
print("List Iteration")
l = ["i", "for", "joy"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("heaven", "for", "hell")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "golden"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['x'] = 1
d['a'] = 3
for i in d:
    print("%s  %d" % (i, d[i]))