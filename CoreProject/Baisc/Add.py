# a = 5
# b = 9
# c = a+b
#
# print("addition",c)
# print(type(a))
#
#
#
#
#
# import datetime
#
# today = datetime.date.today()
# future = today + datetime.timedelta(days=7)
# past = today - datetime.timedelta(days=7)
#
# print("7 days later:", future)
# print("7 days ago:", past)
#
#
#
#
#
# import datetime
#
# today = datetime.date.today()
# future = today + datetime.timedelta(days=7)
# past = today - datetime.timedelta(days=7)
#
# print('future dayes of 7',future)
# print('past of 7 days',past)

class Employee:
    'I am Employee'

    def __init__(self, salary):
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


emp = Employee(2000)

print(emp)

print(id(emp))

print(emp.__doc__)
