import json
x = {
    "name":"john",
    "age":30,
    "city":"newyork"
}
y = json.dumps(x)
print(y)
print(type(y))
print(x)
print(type(x))