# Python RegEx
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
    print("Yes, we have a match")
else:
    print('No Match')

# There're lots of rules etc that you can look up