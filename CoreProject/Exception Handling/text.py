# a = 10
# b = 0
# c = a / b
# print(c)
# print("Hello world")


# a = 4
# b = 0
# try:
#     c = a / b
#     print('C:', c)
# except ZeroDivisionError:
#     print("Check your dividend is zero")
#
# print("Hello world")

# try:
#     c = a / b
#     print('C:', c)
# except ZeroDivisionError as e:
#     print("Excption:", e)
#
# a = 4
# b = 2
# try:
#     c = b / a
#     print('C:', c)
# except ZeroDivisionError:
#     print("Check your dividend is zero")
# finally:
#     print("Your division was greater than zero")
#

# try:
#     a = int(input("Enter value of first number:"))
#     b = int(input("Enter value of second number:"))
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("Division by zero error")
# except ValueError:
#     print("Non-numeric inputs provided")

list = {'name': "anant", 'age': 19}
k = input("Enter key to search:")
d = list.keys()
try:
    v = list[k]
    print("key is present")
except Exception:
    print("key not found")
