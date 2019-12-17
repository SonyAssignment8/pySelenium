def add(a,b):
    return a+b
print(add(1,2))

#by using lambda
z=lambda a,b:a+b
print(z(1,2))

#decorator
def outer(fun):
    def inner():
        print("inner fun")
        fun()
        print("inner fun end")
    return inner()
@outer
def well():
    print("well fun")


