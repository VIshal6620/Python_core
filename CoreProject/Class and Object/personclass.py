class Person:
    count = 0  # Class variable (optional)


    def setName(self, name):
        self.name = name


    def getName(self):
        return self.name


    def setSalary(self, salary):
        self.salary = salary


    def getSalary(self):
        return self.salary


    def setCity(self, city):
        self.city = city


    def getCity(self):
        return self.city


# Creating object
p = Person()
p.setName("Vishal")
print("Name:", p.getName())

p.setSalary("25000")
print("Salary:", p.getSalary())

p.setCity("Dewas")
print("City:", p.getCity())



#     def __init__(self, name, salary, city):
#         self.name = name
#         self.salary = salary
#         self.city = city
#
#     def getname(self):
#         return self.name
#
#     def getsalary(self):
#         return self.salary
#
#     def getcity(self):
#         return self.city
#
#
# p = Person("vishal", "32000", "indore")
# print(p.getname(), p.getsalary(), p.getcity())

