# Printing reverse of string given by user
s = input("Enter any string data:")
print(s[::-1])

# Printing numbers from 1 to 10
for i in range(1,11,1):
    print(i, end= " ")

# Printing numbers which is divisible by 3
for i in range(5, 25):
    if i % 3 == 0:
        print(i)
        continue