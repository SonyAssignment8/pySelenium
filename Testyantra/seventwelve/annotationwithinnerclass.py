# Decorator
def outer(fun):
    def inner():
        print("Inside Inner")
        fun()
    return inner()
@outer
def wish():
    print("Good Morning")
