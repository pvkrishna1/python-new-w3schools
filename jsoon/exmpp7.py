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

y = json.dumps(x,indent=4,sort_keys=True)
print(y)