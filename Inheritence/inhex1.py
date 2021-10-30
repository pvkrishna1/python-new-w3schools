# Create a class named Person, with firstname and lastname properties, and a printname method

class Person:
    def __init__(self,fname,lname):
        self.lname = lname
        self.fname = fname

    def printname(self):
        print(self.fname, self.lname)

x = Person( "John", "Doe")
x.printname()

