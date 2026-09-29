from A import A
class B(A):
    def abc(self):
        print("I am Abc")

    def __init__(self,age,**kw):
        super().__init__(**kw)
        self.age = age
        print("b constructor")

