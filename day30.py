# Python Loops 3
# For loops
# range() function
for i in range(100): # from 0 to 99
    if i%3 == 0:
        print(i, end=' ')

for i in range(2,6): # from 2 to 5
    print(i, end='/')

for i in range(2,30,3): # from 2 to 29 with a step size of 3
    print(i)
else: # after finishing the for loop
    print('finished this for loop')

# else is useful when using break/continue statements

# Nested Foor Loops
# For example, used to construct a grid
for x in range(1,10):
    for y in range(1,10):
        print(x+y, end=' ')
    print()

# the above output is funny looking, lool