#multiple
class c1():
    def client1(self):
        print("hiiii")
class c2():
    def client2(self):
        print("hello")
class c3(c1,c2):
    def client3(self):
        print("Hi,hello")
o = c3()
o.client3()
o.client1()
o.client2()