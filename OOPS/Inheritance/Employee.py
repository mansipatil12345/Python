class employee: 
    def __init__(self,id,name): 
        self.id=id 
        self.name=name 

    def display(self): 
        print(f"employe data :\n{self.name}\n{self.id}")