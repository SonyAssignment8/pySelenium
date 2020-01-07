#Program for method overriding?
#Parent class
class Parent():
    def __init__(self):
        self.value = 4

    def get_value(self):
        return self.value

#child class
class Child(Parent):
    def get_value(self):
        return self.value + 1


c = Child()
print(c.get_value())