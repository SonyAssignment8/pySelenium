class c1() :
    def client1(self):
        print("hiiiiii")
class c2(c1) :
    def client2(self):
        print("hello")
class c3(c2,c1):
    def client3(self):
        print("hi hello")
o=c3()
o.client1()
o.client2()
o.client3()