# Python Arrays 2
arry = ['sa', 2, 'lam', 343]
# adding an element
arry.append('abdu')

for i in arry:
    print(i)

# deleting last element (poping)
arry.pop() # it returns the deleted element
print(arry)
# specify an element to be deleted
arry.remove(2)
print(arry)
# it only remove the first occurence

# many other methods exist, such as
# extend(), copy(), index(), ..etc