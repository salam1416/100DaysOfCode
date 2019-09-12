# More dictionaries

dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
dict2 = dict1

dict1['e'] = 5

print(dict2)

# copying that way is just referencing
# to actually copy, use .copy()

dict3 = dict1.copy()

dict1['f'] = 6

print(dict3)
print(dict1)

dict4 = dict(dict1) # another way to copy

# nested dictionaries
dict5 = {'a':{'b':1, 'c':2}}
print(dict5)
# many more methods exist as well, such as
# fromkeys(), get(), items(), update()