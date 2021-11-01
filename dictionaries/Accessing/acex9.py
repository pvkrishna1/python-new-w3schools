
car = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}

x = car.items()
print(x)            # Before changing
car["Year"] = 2020
print(x)            # After chnaging