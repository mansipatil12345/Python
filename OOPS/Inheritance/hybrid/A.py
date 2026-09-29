class A:
    def xyz(self):
        print("I am xyz")

    def __init__(self,name,**kw):
        self.name = name
        print("a const")