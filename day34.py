# Python Function 2
def aFun(nums):
    for i in nums:
        print(i)

N = [3,5,2,5,29,21]
aFun(N)

# you could specify the input of a function

def aFun2(num1, num2, num3):
    return num1+num2*num3

print(aFun2(num2 = 5, num3 = 9, num1 = 43))

# unlimited input

def aFun3(*kids):
    print('The youngest child is '+ kids[2])

aFun3('ali', 'ahmed', 'moh', 'hadi') # it took the third item
# however, all items must be of the same type

# Recursion
# be careful not run into infinite loops

def tri_recursion(k):
    if k>0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print('\n Recursion Example Results ')
tri_recursion(6)