# class Person:
#
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
# p = Person("vishal", "10000000", "Dewas")
# print(p.getname(), p.getsalary(), p.getcity())


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

p = Person("vishal",20)
print(p.getname(),p.getage())
