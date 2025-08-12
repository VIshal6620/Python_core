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



# class Person:
#     def __init__(self,name=None,age=None):
#         self.name = name
#         self.age = age
#
#     def setname(self,name):
#         self.name = name
#
#     def getname(self):
#         return self.name
#
#     def setage(self, age):
#         self.age = age
#
#     def getage(self):
#         return self.age
#
# p = Person()
# p.setname('jatin')
# print(p.getname())
#
# p.setage(85)
# print(p.getage())


