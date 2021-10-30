
def myfunc(n):
    return  lambda a : a * n

mydoubler = myfunc(2)
mydoubler = myfunc(3)

print(mydoubler(3))
print(mydoubler(2))
