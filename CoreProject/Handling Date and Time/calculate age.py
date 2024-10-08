from datetime import date

birth_year = int(input("enter your birth year "))

current_year = date.today().year
time = current_year - birth_year

print(f"you are {time} years old")