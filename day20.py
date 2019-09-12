# Python Sets
thisset = {'apple', 'banana', 'cherry'}
print(thisset)
# sets don't have repeated values
tryset = {1,1,1,3,4,5,6,6,7,7}
print(tryset)
# you cannot access set items with indicies, but you can with for loops
for i in thisset:
    print(i)

# check if itemm is in the set
if 1 in tryset:
    print('1 is in the set')

# Once you create a set, you cannot change the set items

# Adding an item to a set
tryset.add(10)
print(tryset)

# adding more than one item
tryset.update([11,12,13,14])
print(tryset)

