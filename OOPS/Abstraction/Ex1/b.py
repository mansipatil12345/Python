from OOPS.Abstraction.Ex1.a import a
class B(a):
    def show(self):
        print("hello everyone")

obj = B()
obj.show()