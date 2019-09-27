# Applying Lambda
lst = [-4,-6,-5,-1,2,3,7,9,88]
x = lambda ls : ls if ls > 0 else None
for i in lst:
    if x(i) != None:
        print(x(i))




