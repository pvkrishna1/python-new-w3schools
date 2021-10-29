import json

x = '{ "name":"jhon", "age":30, "city":"newyork"}'
y = json.loads(x)
print(y["age"])
print(y)
print(x)