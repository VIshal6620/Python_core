class Person:
    def __init__(self,name=None,age=None):
        self.name = name
        self.age = age

    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

    def setage(self, age):
        self.age = age

    def getage(self):
        return self.age

p = Person()
p.setname('jatin')
print(p.getname())

p.setage(85)
print(p.getage())