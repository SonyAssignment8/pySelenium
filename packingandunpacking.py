def sample():
    print(a, b, c)
sample(*"hai")
sample(*[1,2,3])
sample(*(1, 2 ,3))
sample(*({'a':1 'b':2 'c':3}))
sample(**({'a':1 'b':2 'c':3}))
        # half is pending
