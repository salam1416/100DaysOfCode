# Json thing
import json
tup = ('Saturday', 'Sunday', 'Monday', 'Tuesday',
'Wednesday', 'Thursday', 'Friday')

to_json = json.dumps(tup)
print(to_json)
print(type(to_json))