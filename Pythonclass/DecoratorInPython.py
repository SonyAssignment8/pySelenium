def outer(fun):
    def inner():
        print('inside inner')
        fun()
    return inner
@outer
def wish():
    print('good morning')
wish()
#outer(wish())    # 2nd directly we can call without @outer annotation