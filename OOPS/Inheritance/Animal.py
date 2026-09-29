class Animal:
    #class var of parent
    category ="Animal"

    #def con of parent have higher scope or get called when no 
    #const is declared in child class 
    def __init__(self):
        print("Animal def con called!")
    #para con of parent: only execute when it gets called using super()
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
    #instance method of parent
    #child can access it 
    def eat(self):
        print("eating.....")