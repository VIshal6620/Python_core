class Person:

# #    count = 0
    #
    #     def setName(self, name):
    #         self.name = name
    #
    #     def getName(self):
    #         return self.name
    #
    #     def setsalary(self, salary):
    #         self.salary = salary
    #
    #     def getsalary(self):
    #         return self.salary
    #
    #     def setcity(self, city):
    #         self.city = city
    #
    #     def getcity(self):
    #         return self.city
    #
    #
    # p = Person()
    # p.setName("vishal")
    # print(p.getName())
    # p.setsalary("25000")
    # print(p.getsalary())
    # p.setcity("dewas")
    # print(p.getcity())
    #
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


p = Person("vishal", "32000", "indore")
print(p.getname(), p.getsalary(), p.getcity())

