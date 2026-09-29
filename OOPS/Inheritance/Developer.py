from Employee import employee 
class developer(employee): 
    def __init__(self,working_hrs,id,name): 
        super().__init__(id,name) 
        self.working_hrs=working_hrs 

    def display_working_hr(self): 
        print(f"working hr is:{self.working_hrs} ")