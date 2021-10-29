import json
x = {
    "name":"john",
    "age":30,
    "married":True,
    "divorsed":False,
    "childern":("ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":17},
        {"model":"FORD EDGE","mpg":25}
    ]
}

print(json.dumps(x))
y=json.dumps(x)
print(y)
print(type(y))
