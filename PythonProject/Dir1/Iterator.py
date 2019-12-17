l = [8,9,7,90,78]
for i in l :
    print(i)

# Pre defined iterator
l = [8,9,7,90,78]
i = iter(l)
next(i)
next(i)
next(i)
next(i)
next(i)

# custom iterator
class Hotel():
    def __init__(self):
        self.menu = ['Idli','Dosa', 'Vada']
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if self.index >= len(self.menu):
            raise StopIteration
        return self.menu[self.index]

for i in Hotel():
    print(i)
