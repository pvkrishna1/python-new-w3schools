
car = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}

x = car.values()
print(x)            # Before Changing
car["Year"] = 2020
print(x)          # After Changing
