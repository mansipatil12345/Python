from p import p 
class c1(p):
    pass

    #method 1 to implement
    # def add(self,a,b,c=0):
    #     return(a+b+c)

    #method 2 using keyword argument
    def add(self,*args):
        return(sum(args))

obj = c1()
    