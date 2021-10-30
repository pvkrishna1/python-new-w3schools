# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print( self.fname, self.lname)

class Student(Person):
    pass

x = Student( "Mike", "Olsen")
x.printname()
