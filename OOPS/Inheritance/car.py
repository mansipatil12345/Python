from engine import engine
class car:
    def __init__(self):
        self.e = engine()

    def start_car(self):
        print("Car is going to start ")
        self.e.start()
        print("Car is started")

c = car()
c.start_car()
c.e.engine_details()

