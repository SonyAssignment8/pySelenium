class C1():
    def client1(self):
        print('hiiii')
class C2(C1):
    def client2(self):
        print('Hello')
class C3(C1):
    def client3(self):
        print('Hi Hello')
class C4(C2,C3):
     def client4(self):
        print('Hi Hello Bye')
O = C4()
O.client1()
O.client2()
O.client3()
O.client4()