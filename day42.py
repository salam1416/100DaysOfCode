# Python CLasses and Objects 2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print('Hello my name is ' + self.name)
    
p1 = Person('John', 36)

# change class variable
p1.age = 40

print(p1.age)

# delete member variable
del p1.age

# print(p1.age) # will get an error

# delete class instance (Object)
del p1

# print(p1) # will get an error
