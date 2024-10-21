class Shape():

    def __init__(self, color, borderwidth):
        self.color = color
        self.borderwidth = borderwidth

    # def setcolor(self, color):
    #     self.color = color

    def getcolor(self):
        return self.color

    # def setborderwidth(self, borderwidth):
    #     self.borderwidth = borderwidth

    def getborderwidth(self):
        return self.borderwidth


class Circle(Shape):
    def __init__(self, radius, color, borderwidth):
        super().__init__(color, borderwidth)
        self.radius = radius

    def getradius(self):
        return self.radius

    def Area(self):
        return 3.14 * self.radius


c = Circle(6, "White", 20)
print("Color of Radius =", c.getcolor())
print("borderwidth of Radius =", c.getborderwidth())
print("Area of Circle=", c.Area())

# class Shape:
#     def __init__(self, color, borderwidth):
#         self.color = color
#         self.borderwidth = borderwidth
#
#     def getcolor(self):
#         return self.color
#
#     def getborderwidth(self):
#         return self.borderwidth
#
#
# class Circle(Shape):
#     def __init__(self, radius, color, borderwidth):
#         super().__init__(color, borderwidth)
#         self.radius = radius
#
#     def getradius(self):
#         return self.radius
#
#     def Area(self):
#         return 3.14 * (self.radius ** 2)
#
#
# c = Circle(6, "White", 20)
# print("Color of Circle =", c.getcolor())
# print("Border width of Circle =", c.getborderwidth())
# print("Area of Circle =", c.Area())
