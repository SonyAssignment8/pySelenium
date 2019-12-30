def sample():
    yield 1
    yield 2
    yield 3

s=sample()
i=s.__iter__()
print(next(i))
print(next(i))
print(next(i))
#print(next(i))  #Stop the iteration