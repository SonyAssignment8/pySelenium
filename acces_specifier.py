class A:
    __name="anna"
    def display(self):
        print(A.__name)

    def get__display(self):
        return self.__name

    def set__display(self,name):
        self.name_1=name
        print(self.name_1)
a=A()
a.display()
a._A__name="World"
#print(a._A__name) #to access private variable outside the class
print(a.get__display())
a.set__display("hello")


