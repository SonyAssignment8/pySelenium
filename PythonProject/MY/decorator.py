def outer(fun):
    def inner():
        print('inside inner')
        fun()
    return inner
@outer
def wish():
    print("inside wish")
wish()
@outer
def order():
    print("inside order")
order()
