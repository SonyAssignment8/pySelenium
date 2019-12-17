class Fibonac():
    a = 0
    b = 1
    print(a, end=" ")
    print(b,end=" ")
    c = a+b
    for i in range(1, 10, 1):
        print(c, end=" ")
        a = b
        b = c
        c = a + b