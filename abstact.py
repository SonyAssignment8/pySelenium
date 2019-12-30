import abc

class A:
    def disply(self):
        print("this is a")

class B(A):
    def display(self):
        print("this is b")

a=B()
a.display()
a.disply()
