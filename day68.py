# formatting
name =  'Ahmed Ali'
balance = 53.44
print('Dear {}, Your current balanec is {} $'.format(name, balance))

######## extra
print() 
n = int(input('Enter the number of elements: '))
lst = []
for i in range(n):
    st = 'What is the ' + str(i+1) + ' element? '
    x = input(st)
    lst.append(x)

print('your elements were ', lst)


