#we will test how json (java script object notation) works with python together.
#first we need to import json module
import json
jsonstring = '{"name": "javier", "age": 59, "married": True}'
#we use json.loads() for converting and parsing (decoding) from json to python:
person = json.loads(jsonstring)
print(person['name'], 'is', person['age'], 'years old')


