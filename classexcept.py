class NameException(Exception):
    def __init__(self,msg=None):
        self.msg=msg
    def __str__(self):
        return "exception is because of\"" \
               +str(self.msg)
try:
    raise NameException(123)
except Exception as e:
    print(e)