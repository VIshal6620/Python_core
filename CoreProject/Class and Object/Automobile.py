class person:


        def setcolor(self, color):
            self.color = color

        def getcolor(self):
            return self.color

        def setSpeed(self, Speed):
            self.Speed = Speed

        def getSpeed(self):
            return self.Speed

        def setMake(self, Make):
            self.Make = Make

        def getMake(self):
            return self.Make


p = person()
p.setcolor("white")
print(p.getcolor())
p.setSpeed("80")
print(p.getSpeed())
p.setMake("Car")
print(p.getMake())




