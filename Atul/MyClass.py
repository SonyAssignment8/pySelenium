class MyClass():
    variable ="blah"
    def function(self):
        print("This Is Msg Inside Class")
myobjectx = MyClass()  # assign the above class(template) to an object you
# Now the variable "myobjectx" holds an object of the class "MyClass"
print(myobjectx.variable)
myobjecty = MyClass()
myobjecty.variable="blah blah"
print(myobjecty.variable)
print("------------------------function call--------------------------")
myobjectx.function()
