class person:
    #     def setcolor(self, color):
    #         self.color = color
    #
    #     def getcolor(self):
    #         return self.color
    #
    #     def setSpeed(self, Speed):
    #         self.Speed = Speed
    #
    #     def getSpeed(self):
    #         return self.Speed
    #
    #     def setMake(self, Make):
    #         self.Make = Make
    #
    #     def getMake(self):
    #         return self.Make
    #
    #
    # p = person()
    # p.setcolor("white")
    # print(p.getcolor())
    # p.setSpeed("80")
    # print(p.getSpeed())
    # p.setMake("Car")
    # print(p.getMake())

    def __init__(self, fname, lname, city):
        self.fname = fname
        self.lname = lname
        self.city = city

    def getfname(self):
        return self.fname

    def getlname(self):
        return self.lname

    def getcity(self):
        return self.city
p=person("vishal","vishwakarma","indore")
print(p.getfname(),p.getlname(),p.getcity())
