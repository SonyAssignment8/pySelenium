class One():
    def __init__(self):
        self.a=10
        self.b='hi'
    def method1(self):
        print("method one")
class Two(One):
    def __init__(self):
        self.c=3

    def method1(self):
        print("method2")
o=Two()
o.method1()
o1=One()
o1.method1()
