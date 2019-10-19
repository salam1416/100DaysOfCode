# searching with regex
import re

strr = 'data is the new oil'

y = re.search('^data', strr)
print(y)
print(y.group())