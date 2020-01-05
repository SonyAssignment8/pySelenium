# Python Specific
# 1.How will run the python program using pytest?
# python -m pytest filename.py

# 2.What is the need of exception? Write the syntax for exception?
# The core advantage of exception handling is to maintain the normal flow of the application.
# An exception normally disrupts the normal flow of the application that is why we use exception handling.
# try:
#     print("this is try block")
# except:
#     print("some error")

# 3. How to generate report in pytest?
# python -m pytest -allure-dir
# allure-serve "filename"

# 4. How will make function protected in python?


# 4. Try and except? Exception Handling
try:
    n1=int(input("Enter a number"))
    n2=int(input("Enter a number"))
    res=n1/n2
except ZeroDivisionError as E:
    print("Exception",E)

# 5. What is the Use of @?

# 6. What is CI/CD?
# Continuous integration is a coding philosophy and set of practices that drive development teams to implement small changes and
# check in code to version control repositories frequently. Because most modern applications
# require developing code in different platforms and tools, the team needs a mechanism to integrate and validate its changes.

# 7. What are pytest fixtures?
# The purpose of test ﬁxtures is to provide a ﬁxed baseline upon which tests can reliably and
# repeatedly execute. pytest ﬁxtures offer dramatic improvements over the classic xUnit style of setup/teardown functions:
# • ﬁxtures have explicit names and are activated by declaring their use from test functions, modules, classes or whole projects.
# • ﬁxtures are implemented in a modular manner, as each ﬁxture name triggers a ﬁxture function which can itself use other ﬁxtures.
# • ﬁxture management scales from simple unit to complex functional testing, allowing to parametrize ﬁxtures and tests according to conﬁguration and
# component options, or to re-use ﬁxtures across function, class, module or whole test session scopes.

# 8. How to debug the code?
# After you have configured a run configuration for your project, you can launch it in debug mode by pressing Shift+F9.
# In the Debug tool window you can see the list of frames and threads with their states, variables and
# watches. When you select a frame, you see the variables corresponding to the selected frame.

# 9.Difference between mutable and immutable?
# The variable, for which we can change the value is called mutable variable.
# list,dict,set,bytearray,user - defined classes(unless specifically made immutable) are mutable
#
# The variable, for which we can not change the value is immutable variable.
# int,float,decimal,complex,bool,string,tuple,range are immutable

# 10. Use get_page_source () and store output in a file and count particular word in that file


# 11. How can you call the method of the class which is present in other file
# from filename1 import func1

# 12.Can we overload operators
# Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator.
# For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.
class A:
    def __init__(self, a):
        self.a = a
        # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("hello")
ob4 = A("world")
print(ob1 + ob2)
print(ob3 + ob4)


# 13.What are magic methods?
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
# Dunder here means “Double Under (Underscores)”.
# These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

# 14. How to remove duplicate values in a dictionary?
data={'a':1,'a':2,'c':3,'a':1,'c':3,'b':2}
result = {}
for key,value in data.items():
    if value not in result.values():
        result[key] = value
print(result)

# 15. Can you overload operator?
# Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator.
# For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.
class A:
    def __init__(self, a):
        self.a = a
        # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("hello")
ob4 = A("world")
print(ob1 + ob2)
print(ob3 + ob4)

# 16. Can method be overloaded in python?
# Like other languages (for example method overloading in C++) do, python does not supports method overloading.
# We may overload the methods but can only use the latest defined method.
# However we may use other implementation in python to make the same function work differently i.e. as per the arguments
def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c
# add(1,3)
print(add(4,6,8))

# 17. Syntax to import a module
# from package_name import module

# 18.  How to handle json file?
import json
f=open("file.txt","w")
data={'a':"apple",'b':"berry"}
json_data=json.dumps(data)
# print(json_data)
a=f.write(json_data)
print(a)
print("success")
f.close() #to write data into json and encrypted the data

# f=open("file.txt","r")
# data=f.read()
# print(json.loads(data))
# f.close() #to read data from json  and decrypted to original data


# 19. What is Decorator? Give example
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
def outer(display):
    def inner():
        print("inside the in function")
        display()
        print("after dispaly")
    return inner
@outer
def display():
    print("inside display")
display()

# 20.What is yield?
# Yield is a keyword that is used like return , except the function will return a generator.
# The first time the for calls the generator object created
# from your function, it will run the code in your function from the beginning
# until it hits yield , then it'll return the first value of the loop

# 21.What is polymorphism?
# the word polymorphism means having many forms.
# In programming, polymorphism means same function name (but different signatures) being uses for different types.
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))

# 22.Is Method Overloading supported in python?
# Like other languages (for example method overloading in C++) do, python does not supports method overloading.
# We may overload the methods but can only use the latest defined method.
# However we may use other implementation in python to make the same function work differently
def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c
# add(1,3)
print(add(4,6,8))

# 23.What is Regular Expression?
# A regular expression is a special sequence of characters that helps you
# match or find other strings or sets of strings, using a specialized syntax held in a pattern.
# Regular expressions are widely used in UNIX world.
# The Python module re provides full support for Perl-like regular expressions in Python.
# The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

# 24.Which version of python u have used in your current project
# python 3.4 to python 3.6

# 25. What is List comprehension?
# List comprehension is an elegant way to define and create list in Python.
# These lists have often the qualities of sets, but are not in all cases sets.
# List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce().

# 26.What is Dictionary comprehension?
# A dictionary comprehension takes the form {key: value for (key, value) in iterable}
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
myDict = {k: v for (k, v) in zip(keys, values)}
print(myDict)

# 27. How u will achieve encapsulation, polymorphism and inheritance
# The polymorphism is the process of using an operator or function in different ways for different data input.
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))

# The encapsulation hides the implementation details of a class from other objects.
class Base:
    def __init__(self):
        # Protected member
        self._a = 2
# Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class: ")
#         print(self._a)
# obj1 = Base()
# print(obj1.a)
# obj2 = Derived()

# The inheritance is a way to form new classes using classes that have already been defined
class A:
    pass
class B(A):
    pass
b=B()

# 28.Example for method overriding
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    pass
c = Child()
c.get_value()

# 29. How you will make function protected in python
class Cup:
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None


# 30. Which tool you have used for track the report?

# 31. As daily basis, where you used to store your scripts? How?

# 32. How to fetch the data from external file? Example
#to read the data use for loop
f=open("C:/Users/ankita/PycharmProjects/pgm/ab.txt","r")
for i in range(1,7):
    data=f.readlines(i)
    print(data)
f.close()


# 33. Print frequency of words present in text file.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("file1.txt"))

# 34. Say 1 file is there, you have to search “email” over there and replace with “username”. How will you do that?

# 35. What is filter, map and reduce? Explain with examples.
# syntax of map
# map(func, *iterables)
#
# Where func is the function on which each element in iterables (as many as they are) would be applied on. Notice the asterisk(*) on iterables?
# It means there can be as many iterables as possible, in so far func has that exact number as required input arguments.
#salary increment by 10%
add=lambda sal:sal+10/100*sal
print(list(map(add,[1000,2000,3000])))

# syntax of filter
# While map() passes each element in the iterable through a function and
# returns the result of all elements having passed through the function,
# filter(), first of all, requires the function to return boolean values (true or false) and
# then passes each element in the iterable through the function, "filtering" away those that are false.
# filter(func, iterable)
#even numbers
print(list(filter(lambda n:n%2==0,[11,22,33,44])))
#palidrome
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

# syntax of reduce
# reduce applies a function of two arguments cumulatively to the elements of an iterable,
# optionally starting with an initial argument. It has the following syntax:
#
# reduce(func, iterable[, initial])
#
# Where func is the function on which each element in the iterable gets cumulatively applied to, and
# initial is the optional value that gets placed before the elements of the iterable in the calculation,
# and serves as a default when the iterable is empty.
# The following should be noted about reduce():
# 1. func requires two arguments, the first of which is the first element in iterable (if initial is not supplied) and
# the second the second element in iterable. If initial is supplied, then it becomes the first argument to func and
# the first element in iterable becomes the second element.
# 2. reduce "reduces" (I know, forgive me) iterable into a single value.

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]

# 36. How you will insert elements in a list? Explain with examples.
l=[2,6,7,8,9]
l.append(10)
print(l)

# 37. Difference between list and set?
# Lists and tuples are standard Python data types that store values in a sequence.list=[] or list() list is mutable
# Sets are another standard Python data type that also store values.  set={} or set() whereas set is inmutable
# The major difference is that sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values

# 38. What is dictionary comprehension? Explain with an example.
# A dictionary comprehension takes the form {key: value for (key, value) in iterable}
# create list of fruits
fruits = ['apple', 'mango', 'banana','cherry']
# dict comprehension to create dict with fruit name as keys
print({f:len(f) for f in fruits})

