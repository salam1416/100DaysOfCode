# Python json 2

import json

x = {
    'name':'john',
    'age':30,
    'married':True,
    'divorced':False,
    'children':('Ann', 'Billy'),
    'pets': None,
    'cars':[
        {'model':'BMW 230', 'mpg':25.4},
        {'model':'Ford Edge', 'mpg':23.5}
    ]
}

print(json.dumps(x, indent = 4, separators=(". ", " = "), sort_keys=True))