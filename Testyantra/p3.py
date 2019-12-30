class Employment() :

    Government = 'Govt'
    Private = 'PVT'

    def government (self):
        print("I am Government employee", self.Government)
        print(" I am Govt emp so i have to do less work")

    def private (self):
        print("I am Private employee", self.Private)
        print(" I am Private emp so i have to do more work")

e= Employment ()
e.government()
e.private()