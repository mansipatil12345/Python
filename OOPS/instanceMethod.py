class demo:
    #inst var ---> init method ---> var intialize
    def __init__(self,name,course):
        self.name = name
        self.course = course

    #inst method --> self--> completely depends upon object
    def display(self):
        print(self.name,self.course)

s1=demo("ram","pfs")
s1.display()
s2=demo("sita","jfs")
s2.display()
