
def myfunc(n):
    return lambda a : a * n

multiplyer = myfunc(3)

print(multiplyer(11))