def myfunc():
    x = 300
    def myinner():
        print(x)

    myinner()

myfunc()