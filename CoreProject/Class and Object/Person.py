class Person:

    def __init__(self, name, salary, city):
        self.name = name
        self.salary = salary
        self.city = city

    def getname(self):
        return self.name

    def getsalary(self):
        return self.salary

    def getcity(self):
        return self.city


p = Person("vishal", "10000000", "Dewas")
print(p.getname(), p.getsalary(), p.getcity())
