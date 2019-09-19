# Python Functions
# Built-in functions; such as len(), print(), etc
# User-defined functions; such as below

def afunction(a,b):
    print(a+b)

afunction(2,3)

def emailCompletion(user):
    '''
    This function complete a string
    '''
    return user + '@gmail.com'

print(emailCompletion('salam'))

# default values (optional input)
def deff(a=12):
    return a*a

print(deff()) # defulat input will be used
print(deff(3)) # input of 3

