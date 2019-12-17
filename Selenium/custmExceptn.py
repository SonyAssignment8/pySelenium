# Custom exception
class NameException(Exception):

    def __init__(self, msg=None):
        self.message = msg

    def __str__(self):
        return "Exception is because of "+ str(self.message)

try:
    raise NameException(1323)
except NameException as e:
    print(e)
