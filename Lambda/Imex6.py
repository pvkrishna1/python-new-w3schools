def myfunc(n):
    return lambda a : a*n

multiplier = myfunc(3)

print(multiplier(11))