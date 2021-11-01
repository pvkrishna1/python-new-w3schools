
car = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}

x = car.items()
print(x)                   # Before chnaging
car["colour"] = "Red"
print(x)                # After changing