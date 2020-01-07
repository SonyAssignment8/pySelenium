#Write a program for custom iterato
class Car():
    def __init__(self):
        self.name=['maruthi','scoda','XUV','Benz']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.name):
            raise StopIteration
        print(self.name[self.index])
c=Car()
c.__next__()
c.__next__()
c.__next__()
c.__next__()
