class Account:

    # def setNumber(self, Number):
    #         self.Number = Number
    #
    #     def getNumber(self):
    #         return self.Number
    #
    #     def setActype(self, Actype):
    #         self.Actype = Actype
    #
    #     def getActype(self):
    #         return self.Actype
    #
    #     def setBalance(self, Balance):
    #         self.Balance = Balance
    #
    #     def getBalance(self):
    #         return self.Balance
    #
    #
    # p = Person()
    # p.setNumber("89011000660066")
    # print(p.getNumber())
    # p.setActype("Saving")
    # print(p.getActype())
    # p.setBalance("10000000")
    # print(p.getBalance())

    def __init__(self, Actype, balance, number):
        self.Actype = Actype
        self.balance = balance
        self.number = number

    def getActype(self):
        return self.Actype

    def getbalance(self):
        return self.balance

    def getnumber(self):
        return self.number


p = Account("saving", 1000000, 89001100006485)
print(p.getActype(),p.getnumber(),p.getbalance())
