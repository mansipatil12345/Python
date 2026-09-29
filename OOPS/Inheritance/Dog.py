#step1: import to use 
from Animal import Animal
# pass object of parent to child to reuse code of parent class
class Dog(Animal):
    #instance method of child class
    def bark(self):
        print("dog is barking.....")
    # def con of child
    def __init__(self):
        print("dog def con called!")
    #para con of child class
    def __init__(self,name,breed,color):
        #super() is used to initialize to parent properties/constructor
        super().__init__(breed,color)
        self.name = name

d1= Dog()
d1.bark()
d1.eat()