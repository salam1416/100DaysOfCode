# Python sets 2
set1 = {1,2,3,4,5}
print(set1)
print(len(set1)) # length of set
set1.remove(2) # remove an element
set1.discard(3) # remove an element
# the difference between the two methods is that discard won't show an error if the element doesn't exist
print(set1)
set1.pop() # remove the last element
print(set1)
del set1 # delete the whole set

# print(set1) # will raise an error

set2 = set([1,2,2,3,4,5,6,6]) # another way of building a set

# there're also other methods in set(); such as 
# add(), clear(), copy(), difference()
# ... etc look up documentation
