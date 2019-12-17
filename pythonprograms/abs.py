# class A():
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         pass

from abc import ABC,abstractmethod
class B(ABC):
    @abstractmethod
    def m2(self):
        pass
class C(B):
    def __init__(self):
        self.a=10
b=B()

