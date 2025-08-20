import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

# The Strftime()
import datetime
x=datetime.datetime(2019,9,6)
print(x.strftime("%B"))



from datetime import date

# Get the user's birth year
birth_year = int(input("Enter your birth year: "))

# Get the current year
current_year = date.today().year

# Calculate the age
age = current_year - birth_year

 # Print the result
print(f"You are {age} years old.")

