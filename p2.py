'''def add(a,b):
    return a+b
add(2,4)'''

add=lambda a,b:a+b
print(add(4,6))

def sam():
    print("first")
    yield
    print("second")
    yield
    print("third")
    yield
    print("fourth")
    yield
    print("xuyt")
print(sam())

var=sam()
i=iter(var)
next(i)
next(i)
next(i)
next(i)
next(i)


