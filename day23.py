# Dictionaries
thisdict = {'salam':1, 'ali':2, 'hadi':3, 'hussain':4}
print(thisdict)
if 'salam' in thisdict:
    print('salam is in the dictionary')

print(len(thisdict)) # length of keys

# to add an element, just referenced a non-existing key
thisdict['mohammed'] = 5
print(thisdict)

# remove with pop()
thisdict.pop('hussain')
print(thisdict)

anotherdict = thisdict

del thisdict # remove the whole dict

print(anotherdict)

anotherdict.clear() # clear all items from dict()

print(anotherdict)