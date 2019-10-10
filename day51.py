# Python Module 2

# renaming modules
import mymodule as md 
print(md.lst)

# built-in modules
import platform
print(platform.system())
print(platform.python_version())

# list all defined names in platform
print(dir(platform))

# you can import part of a module
from mymodule2 import x
print(x)
# only x is imported from mymodule2
