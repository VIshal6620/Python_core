class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print("Deposited:", amt)
        else:
            print("Amount must be positive.")

    def withdraw(self, amt):
        if amt > 0:
            if amt <= self.balance:
                self.balance -= amt
                print("Withdrawn:", amt)
            else:
                print("Not enough balance.")

    def show_balance(self):
        print("Balance:", self.balance)


def main():
    name = input("Enter your name: ")
    acc = BankAccount(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        ch = input("Choose option: ")

        if ch == '1':
            amt = float(input("Amount to deposit: "))
            acc.deposit(amt)
        elif ch == '2':
            amt = float(input("Amount to withdraw: "))
            acc.withdraw(amt)
        elif ch == '3':
            acc.show_balance()
        elif ch == '4':
            print("Bye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()


#Automobile

#
# class Automobile:
#     def __init__(self, make, model, year, mileage=0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     def drive(self, miles):
#         if miles > 0:
#             self.mileage += miles
#             print(f"Drove {miles} miles.")
#         else:
#             print("Miles driven must be positive.")
#
#     def display_info(self):
#         print(f"Automobile Info:")
#         print(f"Make: {self.make}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#         print(f"Mileage: {self.mileage} miles")
#
#
# def main():
#     print("Welcome to the Automobile Program!")
#
#     make = input("Enter the make of the automobile: ")
#     model = input("Enter the model of the automobile: ")
#     year = input("Enter the year of the automobile: ")
#
#     automobile = Automobile(make, model, year)
#
#     while True:
#         print("\nOptions:")
#         print("1. Drive the automobile")
#         print("2. Display automobile info")
#         print("3. Exit")
#
#         choice = input("Choose an option (1-3): ")
#
#         if choice == '1':
#             miles = float(input("Enter miles to drive: "))
#             automobile.drive(miles)
#         elif choice == '2':
#             automobile.display_info()
#         elif choice == '3':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()
