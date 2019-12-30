#hybrid
class c1():
    def client1(self):
        print("hiii")
class c2(c1):
    def client2(self):
        print("hello")
class c3(c1):
    def client3(self):
        print("hi,hello")

class c4(c2,c3):
    def client4(self):
        print("hiiiiiiiii hellllllloooo")
o = c4()
o.client1()
o.client2()
o.client3()
o.client4()