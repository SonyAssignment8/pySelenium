# Ques-36
a = 5
table = [[a, b, a * b] for b in range(1, 11)]
print("/n Multiplication table")
for i in table:
    print(i)

print(", ".join(["ha" if i else "Ha" for i in range(3)]) + "!")
