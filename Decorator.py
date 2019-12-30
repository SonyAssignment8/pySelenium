def outer(fun):
    def inner():
        print("Inside Inner")
        fun()
    return inner
@outer
def wish():
    print("Hi")

wish()
outer(wish())