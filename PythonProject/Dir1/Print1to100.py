class Recurssion():
    def num(self, i):
        if(i<=100):
            print( 'Numbers',i)
            i+=1
            self.num(i)
r = Recurssion()
r.num(1)