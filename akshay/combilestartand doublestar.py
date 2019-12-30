def sample(*args, **kwargs):
    print(args)
    print(kwargs)
sample()
sample(1, 2, 3 , 4, 5 )
sample(a=1, b=2)
sample(1, 2, 3, a=10, b=20, c=30)

# this wil be used when the no of arguments are unknown.
# this will be used at the time of building the generic code or API


