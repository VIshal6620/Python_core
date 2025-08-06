class Person:
    count = 0  # Class variable (optional)

    # Set name
    def setName(self, name):
        self.name = name

    # Get name
    def getName(self):
        return self.name

    # Set salary
    def setSalary(self, salary):
        self.salary = salary

    # Get salary
    def getSalary(self):
        return self.salary

    # Set city
    def setCity(self, city):
        self.city = city

    # Get city
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

