# Python string formatting

price = 49
txt = 'The price is {:.2f} dollar'
print(txt.format(price))
itemno = 567
quanitity = 3
myorder = 'I want {} pieces of item number {} for {:.2f} dollars'
print(myorder.format(quanitity, itemno, price))