# Python tuples 2
atuple = (1,2,3,4)
if 3 in atuple:
    print('3 is in the tuple')
# repeating an item in a tuple
thistuple = ('apple',)*3 
# without the comma, it's be a string
print(thistuple)
print(atuple + thistuple)

# The example
x = (3,4,5,6)
x = x + (1,2,3)
print(x)

print(len(x))

# Constructors
a = ()
print(type(a))
b = tuple()
c = tuple([1,2,3,4,5])
print(c)

print(1)
print(2)