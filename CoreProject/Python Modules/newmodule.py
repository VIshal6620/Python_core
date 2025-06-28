# import mymodule
# mymodule.greeting("Python")
# import mymodule
# a = mymodule.peron["age"]
# print(a)
# import mymodule as new_module
# a=new_module.person["name"]
# print(a)
# import platform
# x=dir(platform)
# print(x)
# from os import supports_fd
# supports.print_func("Ram")



# Importing and using `mymodule`
import mymodule

# Using the `greeting` function from mymodule
mymodule.greeting("Python")

# Accessing the `person` dictionary from mymodule
try:
    age = mymodule.person["age"]
    print("Age from mymodule:", age)
except AttributeError:
    print("The module 'mymodule' does not have a 'person' dictionary.")

# Using an alias for `mymodule`
import mymodule as new_module
try:
    name = new_module.person["name"]
    print("Name from mymodule:", name)
except AttributeError:
    print("The module 'mymodule' does not have a 'person' dictionary.")

# Exploring the `platform` module
import platform
x = dir(platform)
print("Platform module contents:", x)

# Correct use of `supports_fd` from `os` module
from os import supports_fd

# Example usage
print("Supports file descriptors:", supports_fd)
