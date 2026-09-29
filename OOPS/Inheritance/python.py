from Developer import developer
class pythondeveloper(developer):
    def __init__(self,skill,working_hrs,id,name):
        super().__init__(working_hrs,id,name)
        self.skill = skill

    def work(self):
        print(f"Developer have{self.skill} skill")

    def all_info(self):
        super().display()
        super().display_working_hr()
        self.work()

d1 = pythondeveloper("python","9hr",101,"ram")
d1.display()
d1.display_working_hr()
d1.work()

d1.all_info()