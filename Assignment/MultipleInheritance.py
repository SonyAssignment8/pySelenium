#Multiple Inheritance
class Java():
    def client1(self):
        print('I have Java skills')
class Selenium():
    def client2(self):
        print('I have Selenium skills')

class Resume(Java,Selenium):
    def client3(self):
        print('Resume Method is executed')
o=Resume()
o.client3()
o.client1()
o.client2()