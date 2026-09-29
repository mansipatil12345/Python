from B import B
from C import C
class D(B,C):
    def mno(self):
        print("I am mno")

    def __init__(self,name,city,age,marks):
        super().__init__(
            name = name,
            marks = marks,
            age = age
        )
        self.city=city
        print("D const")

obj = D("ram","pune",20,80)
print(obj.name,obj.city,obj.age,obj.marks)


#key word argument will be used because if two children are accessing are passing the value to same parent like here name is passed to 2 children 
#so will assigning the values through this file its confuse which value to 
# def add(*args):
#     print(sum(args),type(args))
# add(10,20,90,7,)

# k:v
# def info(**kwargs):
#     print(kwargs)
# info(name="ram",age=90)