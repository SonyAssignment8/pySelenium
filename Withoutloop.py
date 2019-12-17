def print100(a):
    if a<=100:
        print(a)
        a+=1
        print100(a)

print100(10)