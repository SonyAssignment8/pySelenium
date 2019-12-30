# l=[1,2,3,4,5]
# i=iter(l)
#Custom Iterator
class Hotel():
    def __init__(self):
        self.menu=['xyz','abc','pp']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.menu):
            raise StopIteration
        print(self.menu[self.index])
h=Hotel()
for i in h:
    print(i)





