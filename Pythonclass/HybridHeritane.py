class c1():
    def client1(self):
        print("client 1")
        cl.client2()
class c2(c1):
    def client2(self):
        print("client 2")
        cl.client3()
class c3(c1):
    def client3(self):
        print("client 3")
        cl.client4()
class c4(c2,c3):
    def client4(self):
        print("client 4")
cl=c4()
cl.client1()
