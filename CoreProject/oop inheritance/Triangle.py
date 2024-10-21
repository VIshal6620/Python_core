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


class Triangle(Shape):

    def __init__(self, base, height, color, borderwidth):
        super().__init__(color, borderwidth)
        self.base = base
        self.height = height

    # def setbase(self, base):
    #     self.base = base

    # def setheight(self, height):
    #     self.height=height

    def getbase(self):
        return self.base

    def getheight(self):
        return self.height  #

    def Area(self):
        return self.base * self.height


t = Triangle(23, 65, "White", 56)
print("Color of Triangle =", t.getcolor())
print("Border width of Triangle =", t.getborderwidth())
print("Area of Triangle =", t.Area())
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
# class Triangle(Shape):
#     def __init__(self, base, height, color, borderwidth):
#         super().__init__(color, borderwidth)
#         self.base = base
#         self.height = height
#
#     def getbase(self):
#         return self.base
#
#     def getheight(self):
#         return self.height
#
#     def Area(self):
#         return 0.5 * self.base * self.height
#
#
# t = Triangle(23, 65, 'red', 56)
# print("Color of Triangle =", t.getcolor())
# print("Border width of Triangle =", t.getborderwidth())
# print("Area of Triangle =", t.Area())
