# Python Regex 3
import re

# replace all white-space characters with the digit 9

strr = "the rain is Spain"
x = re.sub('\s', '9', strr)
print(x)

xx = re.search('ai', strr)
print(xx.span())

yy = re.search(r"\bS\w+", strr)
print(yy.span())

# to print the actual matched string
print(yy.group())