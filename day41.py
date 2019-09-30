# Python Classes and Objects

class MyClass:
    x = 5

print(MyClass)

# Initiating a class
pl = MyClass()
print(pl.x)

# Class properties (member variables)
# and methods (functions)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfun(abc):
        print('Hello my name is ', abc.name)

p2 = Person('John', 36)
p2.myfun()
