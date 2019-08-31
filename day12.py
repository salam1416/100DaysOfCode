a = "Please, I want {} sandwiches and {} donuts"
a = a.replace('I', 'We')
a = a.format(5, 7)
a = a.replace('a','A',len(a) )
print(a)