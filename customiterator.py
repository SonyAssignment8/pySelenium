class Hotel():
    def __init__(self):
        self.menu=["Idli","dosa","puri"]
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.menu):
            raise  StopIteration
        print(self.menu[self.index])

for i in Hotel():
       print(i)

# o =  Hotel()
# i = iter(o)
# next(i)
# next(i)
# next(i)
# or we can do like below:

