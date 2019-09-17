# Python Loops
# While loop
i = 1
while i<20:
    print(i, ' ', end='')
    i+=2
    if i == 11:
        break # this will exit the loop
    elif i == 7:
        continue 

# we could use else with while

a = 4
while a <  10:
    print('a is less than 4')
    a+=4
else:
    print('a', a, 'is not less than 10')

