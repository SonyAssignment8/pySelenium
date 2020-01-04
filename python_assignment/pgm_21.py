# 23 Program for method overriding?
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        print(self.value)
        return 


class Child(Parent):
    pass

c=Child()
c.get_value()
