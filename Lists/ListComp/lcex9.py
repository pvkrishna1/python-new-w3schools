
fruits = [ "apple", "banana", "cherry", "orange", "kiwi", "mango"]

newlist = [ x if x != "banana" else "orange" for x in fruits]

print(newlist)
