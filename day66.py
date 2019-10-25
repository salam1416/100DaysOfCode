# Python string formatting 2

price = 49
itemno = 567
quanitity = 3
myorder = 'I want {0} pieces of item number {1} for {2:.2f} dollars'
print(myorder.format(quanitity, itemno, price))

# another example
age = 36
name = 'John'
txt = 'His name is {1}. {1} is {0} years old'
print(txt.format(age, name)) # interesting

print("my name is {name}".format(name = 'salam'))
