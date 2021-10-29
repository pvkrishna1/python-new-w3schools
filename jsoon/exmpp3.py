import json

print(json.dumps({"name":"john", "age":30}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(("apple","bananas")))
print(json.dumps("hello"))
print(json.dumps(22))
print(json.dumps(3.14))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))