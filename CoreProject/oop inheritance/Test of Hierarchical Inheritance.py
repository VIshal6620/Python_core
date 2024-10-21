class Parent:
    def show(self):
        print("parent method called")

class Child1(Parent):
    def display1(self):
        print("Child1 method called")

class Child2(Parent):
    def display2(self):
        print("Child2 method called")

obj1=Child1()
obj2=Child2()
obj1.display1()
obj1.show()
obj2.display2()
obj2.show()