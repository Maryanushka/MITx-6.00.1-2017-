class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. '+self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Person):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return 'Prof. '+self.name+' says: ' +'I believe that '+ self.name+' says: ' + stuff
    def lecture(self, stuff):
        return 'Prof. '+self.name+' says: ' +'It is obvious that I believe that '+  self.name+' says: ' + stuff



pe = Professor('eric')
ae = ArrogantProfessor('eric')
print(pe.say('the sky is blue'))
print(ae.lecture('the sky is blue'))