# Python Lists
numbers = [1,2,3,4,5]
thislist = ["apple", "banana", "cherry" ]
print(numbers, '\n', thislist)
# indexing
print(thislist[1])
# looping through a list
for i in numbers: 
    print('num ', i)

# changing an item value
numbers[0] = 100
print(numbers)

# deleting an item (or the whole list)
del thislist[0]
print(thislist)