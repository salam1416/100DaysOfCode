# Python tuples
# similar to lists, it uses () instead of []
# it's mutable
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)
oneitem = (3,) # to define one-item tuple, you have to have a comma, otherwise it'll be a number/string
mixed = (1,'text', [1,2,3]) # you can have tuples with mixed types (same as lists, and everything and everything in python basically)
print(mixed[1]) # calling by index
# mixed[0] = 2
# the above code will yield an error beceasue you cannot change an item in a tuple
# also you cannot add an item to it
# once you create it, you cannot change it
del mixed # deleting the whole tuple
