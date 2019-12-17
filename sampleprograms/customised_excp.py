class NameException(Exception):
    def __init__(self,message):
        self.msg=message
    #diretly we cant write print statement so we r overriding str metho
    def __str__(self):
        return "exception is because of "+str(self.msg)
raise NameException(123)