class restaurant:
    def __init__(self, rname):
        self.rname = rname

        self.menu = {
            1: ("Maggi", 100),
            2: ("Coffee", 50),
            3: ("Pasta", 200),
            4: ("Tea", 20),
            5: ("Cake", 300)
        }

    def drd(self):
        print("\nRestaurant Name:", self.rname)

    def display_menu(self):
        print("\n--------- MENU ---------")
        print("ID\tFood\t\tPrice")
        print("------------------------")

        for id, item in self.menu.items():
            print(f"{id}\t{item[0]}\t\t{item[1]}")

        print("------------------------")