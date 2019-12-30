# a=[1,2,3,4]
# i = iter(a)
# # print(next(i))
# # print(next(i))
# for i in i:
#     print(i)


# custom iterator
class Hotel():
    def __init__(self):
        self.menu = ['idli','vada','Dosa']
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.menu):
            raise StopIteration
        return(self.menu[self.index])
# obj = Hotel()
# obj.__next__()
for i in Hotel():
    print(i)




#yield / Generator
