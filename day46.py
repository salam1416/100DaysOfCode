# Day 46 challenge

class Library():
    # default values are added
    def __init__(self, shelf = 0, book = 0):
        self.shelf = shelf # number of shelves
        self.book = book  # number of books

# an example of a Library Object
myLib = Library(shelf = 45, book = 300)

# inherited class
class science_section(Library):
    def __init__(self, name, shelf = 0, book = 0):
        super().__init__(shelf, book)
        self.name = name
    
    def printContent(self):
        print('Section name: ', self.name)
        print('Number of shelves: ', self.shelf)
        print("Number of books: ", self.book)

mysection = science_section(name = 'Physics Books')
mysection.printContent()

# chaning the content 
mysection.book = 20
mysection.shelf = 4
print('\nafter changing the content\n')
mysection.printContent()





