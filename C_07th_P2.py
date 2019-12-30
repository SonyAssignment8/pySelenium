#nested dictionary
# d={'a':{'a1':'apple','a2':'ant'}}
# print(d['a']['a2'][1])

#decorator
def outer(fun):
    def inner():
        print("hiii")
        fun()
    return inner
#return here returns the address
    @outer
    def wish():
        print("hello")
    wish()
    #outer(Wish())
