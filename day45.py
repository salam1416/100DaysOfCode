# Python Iterators
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

# iterating through the items
print(next(myit))
print(next(myit))
print(next(myit))

# strings are iterable as well
s = 'salam'
myits = s.__iter__() # the base constructor
print(myits.__next__())
print(next(myits))
print(next(myits))
print(next(myits))
print(next(myits))

# for loops is an implementation of iterators

# to create an Iterator; it has to have __iter__ and __next__ methods

class MyNumbers:
    def __iter__(self):
        self.a = 1 # first value
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# This for loop would go forever, if we don't StopIteration
#for i in myiter:
#    print(i)

# Here we'll limit the iteration
class MyNumbers2:
    def __iter__(self):
        self.a = 1 # first value
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass2 = MyNumbers2()
myiter2 = iter(myclass2)

for i in myiter2:
    print(i)

# fixing