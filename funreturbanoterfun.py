def outer():
    print("Outer function Started: ")
    def inner():
        print("Inner Function executed")
    print("Outer func returning inner function")
    return inner
f1=outer()
f1()

# or second way is
def outer():
    print("Outer function Started: ")
    def inner():
        print("Inner Function executed")
    print("Outer func returning inner func")
    return inner()                                     # no nedd for last two lines