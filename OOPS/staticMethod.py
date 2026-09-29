class demo:
    @staticmethod
    def add(a,b):
        return a+b

print(demo.add(2,3)) #method 1 can call directly
obj=demo()          #method2 can call using obj also
print(obj.add(90,10))