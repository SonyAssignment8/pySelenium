class C1():
    def client1(self):
        print('hiiii')
class C2():
    def client2(self):
        print('Hello')
class C3(C1,C2):
    def client3(self):
        print('Hi Hello')
O = C3()
O.client1()
O.client2()
O.client3()