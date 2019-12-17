a = 5
table = [[a, b, a * b] for b in range(1, 11)]
print("/n Multiplication table")
for i in table:
    print(i)

# generate a list
li = [i + 1 for i in [1, 2, 3]]
print(li)

# build a list of tuples
li = [(i, i * 2) for i in range(1, 5)]
print(li)

xx = [(i, j) for i in range(1, 6) for j in range(1, 4)]
print(xx)
