
thistuple = ( "apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)

print(thistuple)