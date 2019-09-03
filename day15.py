# Python Lists 3
# list methods
a = [1,2,3,4,5,6]
print(len(a)) # length of list
a.append(7) # adding an item
print(a)
a.insert(2, 'the new item')
print(a)
a.remove(1) # removing an item
print(a)
a.pop() # remove the last item
print(a)
a.clear() # clear the whole list
print(a)
a = [1,2,4,5,6,7]
b = a.copy() # copying a list
b.append(8)
print(a, b)
newlist = [] # list constructor
newlist2 = list() # another constructor
