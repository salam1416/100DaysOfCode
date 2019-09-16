a = 1
b = 34
if b > a:
    print('b is greater thatn a')
elif a == b:
    print(' a equals to b')
else:
    print('b is smaller than a')
# Indentation is used instead of {} in other langauges
# : is used to indicate a code block

# short hand if
if a < b: print('hello')

# short with else
print('hi') if a > b else print('hoo')

# multiple ifs
print('A') if a > b else print('=') if a ==b else print('B')

x = 23
y = 40

# and
if x > 20 and x < 30:
    print('x is between') 
    if x > 21:
        print('x is more than 21')

# OR is similar to and