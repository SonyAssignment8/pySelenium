#single inheritance
class Birds():
    def flying(self):
        print("Birds will fly")
    def eating(self):
        print("Birds are eating")
    def sleeping(self):
        print("Birds are sleeping")

#chlid class
class Parrots(Birds):
    print("parrots")
    def color(self):
         print("Parrots are green in clolor")
    def size(self):
        print("parrots are small in size")
b=Parrots()
b.flying()
b.color()
b.eating()

#Hierarchycal inheritance
class Hen(Birds):
    def color(self):
        print("hens are red and black in color")
    def size(self):
        print("hens are small in size")
h=Hen()
h.flying()
h.color()

#multilevel inheritance
class Chick(Hen):
    def chick(self):
        print("chicks are very cute")
c=Chick()
c.flying()
c.chick()

#multiple inheritance
class Student1():
    def Details1(self):
        print("student 1 details")
class Student2():
    def Details2(self):
        print("student2 details")
class College(Student1,Student2):
    def college(self):
        print("college details")
c=College()
c.college()
c.Details1()
c.Details2()

#hybrid inheritance
class Seniormanager():
    def senoir(self):
        print("senior manager")
class manager1(Seniormanager):
    def manager1(self):
        print("manager one")
class manager2(Seniormanager):
    def manager2(self):
        print("manager two")
class Engineer(manager1,manager2):
    def engineer(self):
        print("engineer")
e=Engineer()
e.senoir()
e.manager2()