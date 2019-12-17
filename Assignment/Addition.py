class Operations():
    a=10
    b=20
    #addition operation
    def add(self):
        print('Addition of two numbers are',Operations.a+Operations.b)

    #Subtraction operation
    def sub(self):
        print('Addition of two numbers are', Operations.a - Operations.b)
def main():
     print('Addition and Subtraction operations are done')
o=Operations ()
o.add()
o.sub()
main()