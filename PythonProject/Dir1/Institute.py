class Institute():
    location = 'Kota'
    I_Name = 'Resonance'
    def coachingType(self):
        print("private")
    def course(self):
        print("JEE preparation")
i = Institute()
print('Coaching Name: ',i.I_Name)
print('Coaching location: ',i.location)
i.coachingType()
i.course()