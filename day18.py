# The first
lst = [1,4,6,3,10,2,19,0]
lst.append(345)
lst2 = lst.copy() # 1
lst2.insert(2,'inserted') # 2
print(lst2)
print('old lst ', lst)
lst.sort() # 3
print('new lst ', lst)
lst2.pop() # 4
print(lst2)
