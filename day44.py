# Python Inheritance 2

# Python inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# We could use super() instead of writing Person, put remove self parameter
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # you could add extra attributes if you want
        self.graduationyear = year
    
    # we could add extra functions
    def welcome(self):
        print('welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)

y = Student('Mike', 'Olsen', 2019)
y.printname() # because it's person as well
print(y.graduationyear)
y.welcome()