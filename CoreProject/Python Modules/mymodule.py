# from importlib import import_module
# import support
# import_module support
#
# print("Hello " + name)
#
# peron = {
#         "name": "Ram",
#         "age": 36,
#         "country": "india"
#     }
# person = {
#         "name": "Ram",
#         "age": 24,
#         "country": "india"
#     }
# from importlib import import_module
# import support
# import_module support


from importlib import import_module

# Importing support module (if needed)
support = import_module('support')

# Example usage of person dictionary
person = {
    "name": "Ram",
    "age": 24,
    "country": "India"
}

# Accessing the 'name' key from the dictionary
print("Hello " + person["name"])

# If you need the older person dictionary, rename it appropriately
older_person = {
    "name": "Ram",
    "age": 36,
    "country": "India"
}

# Print details of both persons
print(f"Person: {person}")
print(f"Older Person: {older_person}")

