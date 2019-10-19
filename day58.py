# Python RegEx 2

import re

# return a list containing every occurences of "ai":

strr = "The rain in Spain"
x = re.findall('ai', strr)
print(x)

xx = re.findall('Portugal', strr)
print(xx)

if (xx):
    print('Yes, there is at least one match')
else:
    print("No match")

xxx = re.search("\s", strr)
print('The first white-space character is located in position: ', xxx.start())

# if no-match, a None will be returned

yyy = re.split("\s", strr)
print(yyy)