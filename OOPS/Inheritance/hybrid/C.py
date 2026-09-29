from A import A
class C(A):
    def pqr(self):
        print("I am pqr")

    def __init__(self,marks,**kw):
        super().__init__(**kw)
        self.marks = marks
        print("C constructor")
