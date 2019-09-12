# Data structures
# Dictionaries
thisdict = {} # empty dictionary
thisdict = {"salam":1, "ali":2}
print(thisdict)
print(thisdict['salam']) # accessing an element
print(thisdict.get('ali'))
# changing an item
thisdict['salam'] = 22
print(thisdict)

for i in thisdict: #looping through a dict()
    print(i) # this will display the keys only
    print(thisdict[i]) # this will display the values only


print(thisdict.values())
print(thisdict.items())

# we could loop through keys and values
for key, value in thisdict.items():
    print(key, value)

