class Hotel():
    def __init__(self):
        self.menu=['Idli','Vada','Pongal','upma']
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
    h.__next__()
