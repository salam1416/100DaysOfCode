# Python Lambda 2
# lambda is very useful as an anonymous function inside another function

def myfun(n):
    return lambda a : a * n

mydoubler = myfun(2)
print(mydoubler(44))

# very interesting