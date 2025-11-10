class Account:

    def setNumber(self, Number):
        self.Number = Number

    def getNumber(self):
        return self.Number

    def setActype(self, Actype):
        self.Actype = Actype

    def getActype(self):
        return self.Actype

    def setBalance(self, Balance):
        self.Balance = Balance

    def getBalance(self):
        return self.Balance


# Correct class name: Account()
p = Account()
p.setNumber("89011000660066")
print(p.getNumber())

p.setActype("Saving")
print(p.getActype())

p.setBalance("10000000")
print(p.getBalance())




