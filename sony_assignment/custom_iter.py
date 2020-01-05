class printNum:
    def __init__(self):
        self.n=0
    def __iter__(self):
        return self
    def __next__(self):

            if self.n>=10:
                raise StopIteration
            else:
                print(self.n)
                self.n += 1

p=printNum()
for i in p:
    p.__next__()