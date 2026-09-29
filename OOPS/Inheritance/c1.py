from p1 import p1
from p2 import p2
class c1(p2,p1):
    #default constructor 
    # def __init__(self):
    #     print("c1 default constructor")
    #     p1.__init__(self)
    #     p2.__init__(self)

    def __init__(self,marks,age,name):
            print("c1 default constructor")
            p1.__init__(self,name)
            p2.__init__(self,age)
            self.marks = marks

    def pqr(self):
        print("c1 pqr")

    def show(self):
        print("c1 show")
        #super().show() #this will call the show method from p2 coz child dont have so it go to p2 first coz in class of c1 p2 is written first then 
                        #if available it prints and stops otherwise go to p1 if not available
        #to print show method from both parent instead of writing super twice will do this 
        p1.show(self)#one que why we used self
        p2.show(self)

# obj = c1()
obj = c1(90,23,"ram")
#obj.xyz()
#obj.abc()
#obj.pqr()
# obj.show()
print(obj.name,obj.age,obj.marks) 


