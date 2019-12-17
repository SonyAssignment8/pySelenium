def sample():
    print(1)
    yield
    print(2)
    yield
    print(3)
    yield
# var = print(sample()) # generator conaitin sequence go to output
#i = iter(var)
# next(i)
# next(i)
# next(i)
var1= sample()
i = iter(var1)
next(i)
next(i)
next(i)
# next(i), if we enable it shows stop iteration .
