#custom exception
class NameException(Exception):
    def __init__(self,message=None):
        self.msg = message
    def __str__(self):
        return "exception is bcoz of "+str(self.msg)
try:
    raise NameException(123)
except NameException as e:
    print(e)