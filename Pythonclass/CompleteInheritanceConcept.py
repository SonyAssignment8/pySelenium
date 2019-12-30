#inheritance and constructor Chaining concept
class Father():
    def __init__(self):
        print("Father Details")
        Father.about(self)
        print("This father has 2 childrens")
    def about(self):
        print("Profession:-Manager in IT Company")
        print("hobies:-playing cricket")
        print("habits:-smoking")
        print("==========================")
class ElderBrother(Father):
    def __init__(self):
        super().__init__()
        print("Elder Son Details")
        ElderBrother.about(self)

    def about(self):
        print("Job:- Governament Employee")
        print("hobies:-playing chess")
        print("smoking,drinking")
        print("==========================")
class YoungerBrother(Father):
    def __init__(self):
        super().__init__()
        print("younger child Details")

    def about(self):
        print("JOB:-Working In IT")
        print("hobies:-playing carrom")
        print("habits:-drinking,smoking,Travelling")
        print("==========================")
class FamilyDetails(ElderBrother,YoungerBrother):
    def __init__(self):
        super().__init__()



fd=FamilyDetails()
fd.about()