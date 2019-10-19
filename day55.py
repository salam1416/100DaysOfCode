# json in Python

import json

# some json
x = '{"name":"john", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary
print(y)

# convert the other way around

xx = {
    'name': 'john',
    'age':30,
    'city':'New York'
}

yy = json.dumps(xx)

print(yy)

# you could also convert other types as well
print(json.dumps(31.44))

# Python | Json
# dict -> Object
# list -> Array
# tuple -> Array
# str -> String
# int -> Number
# float -> Number
# True -> true
# False ->  false
# None -> null