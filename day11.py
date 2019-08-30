# Python Operators 2
# Logical Operators
x = 4
print(x > 2 and x < 10)
print( x < 2 or x > 0 )
print( not(x>3) )
print(x is 4)
print( x is not 3)
x = ['s','m']
y = ['s','m']
print(x is y)
print('s' in x)
print('m' not in y)
# Bitwise operators
# 1 is 01 
# 2 is 10
print(1&2) # should be zero
# 3 is 011
# 7 is 111
print(3&7) # should be 011 which is 3
print(3|7) # should be 111 which is 7
print(~2) #  (-x-1) ss