# Python inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
        

x = Person('john', 'doe')
x.printname()

# Student inherits from Person
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        # you could add extra attributes if you want

y = Student('Mike', 'Olsen')
y.printname() # because it's person as well
