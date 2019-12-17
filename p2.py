class Subjectteacher () :

    History = 'History'
    Civics = 'Civics'
    Maths = 'Maths'
    def teacher (self):
        print("I am maths Teacher")
        print("I am History Teacher........", self.History)
        print("I am Maths Teacher...", self.Maths)
    def students (self):
        print("I AM Student........")

s= Subjectteacher ()
s.Maths
s.students()
s.teacher()