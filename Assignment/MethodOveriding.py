#23 Program for method overriding?
from abc import *
class Electronics(ABC):
    @abstractmethod
    def fan(self):
        pass

class Havells_Remote(Electronics):
    def fan(self):
        print("havells fan is running")

class Crompton_remote(Electronics):
    def fan(self):
        print("Crompton fan is running")


h=Havells_Remote()
h.fan()

