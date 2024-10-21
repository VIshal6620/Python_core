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


class Rectangle(Shape):

    def __init__(self, length,width, color, borderwidth):
        super().__init__(color, borderwidth)
        self.length = length
        self.width = width

    # def setlength(self, length):
    #     self.length = length

    # def setwidth(self, width):
    #     self.width = width

    def getlength(self):
        return self.length

    def getwidth(self):
        return self.width

    def Area(self):
        return self.length * self.width


r = Rectangle(500, 600, "Red", 5)
# r.setborderwidth(10)
# r.setcolor("REd")
# r.setlength(55)
# r.setwidth(80)

print("Color of Rectangle =", r.getcolor())
print("borderwidth of Rectangle =", r.getborderwidth())
print("Area of Rectangle =", r.Area())
