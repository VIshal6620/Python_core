class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f"Current balance: ${self.get_balance():.2f}")


def main():
    account_holder = input("Enter account holder's name: ")
    account = BankAccount(account_holder)

    while True:
        print("Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


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
