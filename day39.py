# Creating power function n^power with recursion
def exponential(power, num):
    if power < 1:
        return 1 # this will exit
    else:
        return num * exponential(power -1, num)

print(exponential(3, 5))







# Recursion is very confusing