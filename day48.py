# Python Score

# Function inside a function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global variables are those which are defined outside of anything 
# like this
t = 545
# t could be accessed from anywhere. 
