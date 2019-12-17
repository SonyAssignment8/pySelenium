class MAX:
    name="MAX"
    discount=40
    branch="bangalore"

    def __init__(self,Name,Age,Phno,Email):
        self.Name = Name
        self.Age = Age
        self.Phno = Phno
        self.Email = Email

    def purchase(self):
        p=input("enter no of items:")
        self.list_items()
        return
    def offer(self):
        pass



