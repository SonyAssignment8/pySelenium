a=[1,2,8,7,9]
i=iter(a)
print(next(i))
print(next(i))

#custom iterator
class Hotel():
    def __init__(self):
        self.menu=['idli','Dosa','vada']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.menu):
            raise StopIteration
        return  (self.menu[self.index])
h=Hotel()
for i in h:
    print(i)