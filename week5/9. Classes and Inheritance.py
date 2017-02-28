# class Clock(object):
#     def __init__(self, time):
# 	    self.time = time
#     def print_time(self, time):
# 	    print(time)
#
# clock = Clock('5:30')
# clock.print_time('10:30')
#
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)
#
# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()
#
# class Weird(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#
# class Wild(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#
# X = 7
# Y = 8
#
# w1 = Weird(X, Y)
# print(w1.getX())
# print(w1.getY())
# w2 = Wild(X, Y)
# print(w2.getX())
# print(w2.getY())
# w3 = Wild(17, 18)
# print(w3.getX())
# w4 = Wild(X, 18)
# print(w4.getX())
# X = w4.getX() + w3.getX() + w2.getX()
# print(X)
# Y = w4.getY() + w3.getY()
# Y = Y + w2.getY()
# print(Y)

# class Spell(object):
#     def __init__(self, incantation, name):
#         self.name = name
#         self.incantation = incantation
#
#     def __str__(self):
#         return self.name + ' ' + self.incantation + '\n' + self.getDescription()
#
#     def getDescription(self):
#         return 'No description'
#
#     def execute(self):
#         print(self.incantation)
#
#
# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Accio', 'Summoning Charm')
#
#
# class Confundo(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Confundo', 'Confundus Charm')
#
#     def getDescription(self):
#         return 'Causes the victim to become confused and befuddled.'
#
#
# def studySpell(spell):
#     print(spell)
#
#
# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())


# class A(object):
#     def __init__(self):
#         self.a = 1
#     def x(self):
#         print("A.x")
#     def y(self):
#         print("A.y")
#     def z(self):
#         print("A.z")
#
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.a = 2
#         self.b = 3
#     def y(self):
#         print("B.y")
#     def z(self):
#         print("B.z")
#
# class C(object):
#     def __init__(self):
#         self.a = 4
#         self.c = 5
#     def y(self):
#         print("C.y")
#     def z(self):
#         print("C.z")
#
# class D(C, B):
#     def __init__(self):
#         C.__init__(self)
#         B.__init__(self)
#         self.d = 6
#     def z(self):
#         print("D.z")
#
# obj = D()
# print(obj.a)
# print(obj.b)
# print(obj.c)
# print(obj.d)
# obj.x()
# obj.y()
# obj.z()