class Factorial():
    def fact(self):
        temp=1
        a=int(input("Enter the value :"))
        for i in range (a,1,-1):
            temp=temp*i
            print(temp)

