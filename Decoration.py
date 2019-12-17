def outer(fun):  # decorator function
    def inner():
        print("its outer class")
        fun()
    return inner()
@outer
def wish():      # function
    print("Hello")
