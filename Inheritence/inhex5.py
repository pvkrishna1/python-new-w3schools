class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationyear=2016

x = Student("Mike","Oslen")
print(x.graduationyear)