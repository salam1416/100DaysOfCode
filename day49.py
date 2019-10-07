# Python Score 2

# variable inside a scope is different that variable outside of it

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

# global words (reserve words)


def myfunc2():
    global c
    c = 200
    print(c)

myfunc2()
print(c) 
# we could see how c inside the function was recognized outside of it after putting global in front of it

# global could also be used to change a variable value from inside another scope
