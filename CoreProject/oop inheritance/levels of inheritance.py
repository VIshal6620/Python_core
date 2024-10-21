#  # single level inheritance
#  class Parent:
#
#      def show(self):
#          print("parent method call")
#
#
#  class Child(Parent):
#      def display(self):
#          print("child method call")
#
#  obj=Child()
#  obj.display()
#  obj.show()
#
# # multi level inheritance
# class GrandParent:
#     def show(self):
#         print("GrandParent method called")
#
#
# class Parent(GrandParent):
#
#     def display(self):
#         print("Parent method called")
#
#
# class Child(Parent):
#     def show_child(self):
#         print("child method called")
#
# obj=Child()
# obj.show_child()
# obj.display()
# obj.show()

# Multiple inheritance

class Parent1:
    def show1(self):
        print("parent method called")


class Parent2:
    def show1(self):
        print("hello")


class Child(Parent1, Parent2):
    def show(self):
        Parent1.show1(self)
        Parent2.show1(self)
    print("c")
obj=Child()
obj.show()
