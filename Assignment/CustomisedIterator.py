#27. Write a program for custom iterator

class Iterator():
    def __init__(self):
        self.car=["maruthi","suzuki","bmw","benz"]
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index=+1
        if self.index>=len(self.car):
            raise StopIteration
        print(self.car[self.index])

i = Iterator()
for j in i:
    print(j)

