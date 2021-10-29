class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is",self.name)
        print("My age is",self.age)

p1 = Person("John",36)
p1.myfunc()
p1.name = "krishna"
p1.age = 25
p1.myfunc()
'''del p1.name                                                                  #comments
p1.myfunc()
del p1.age
p1.myfunc()'''
