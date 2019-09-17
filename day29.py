# Python Loops 2
# for loop
lst = [1,11,2,22,3,33]

# looping through an iterable (such as lists)
for i in lst:
    print(i, end=' ')

print() # a new line

for j in range(10):
    print(j, end='/')
    if j == 7:
        break

print()
for k in 'salam':
    print(k)