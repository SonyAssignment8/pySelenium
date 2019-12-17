def outer():
    print("Outer func started")
    def inner():
        print("Inner function")
    print("outer returning inner function")
    return inner

f1 = outer()
f1()