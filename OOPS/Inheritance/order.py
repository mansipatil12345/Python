from customer import customer
from restaurant import restaurant


class order(customer, restaurant):

    def __init__(self, cname, address, rname):
        customer.__init__(self, cname, address)
        restaurant.__init__(self, rname)
        self.order_history = []

    def take_order(self):

        # Check previous order

        if len(self.order_history) > 0:

            repeat = input("\nDo you want to repeat your previous order? (y/n): ")

            if repeat.lower() == "y":

                food_id = self.order_history[0][0]
                quantity = self.order_history[0][1]

                food_name = self.menu[food_id][0]
                price = self.menu[food_id][1]

                total = price * quantity

                print("\nPrevious Order:")
                print("Food:", food_name)
                print("Quantity:", quantity)

                print("\nOrder Accepted!")

                return

        # New Order

        self.display_menu()

        food_id = int(input("Enter Food ID: "))

        if food_id not in self.menu:

            print("Invalid Food ID")
            return

        quantity = int(input("Enter Quantity: "))

        food_name = self.menu[food_id][0]
        price = self.menu[food_id][1]

        total = price * quantity

        print("\nOrder Accepted!")
        print("Food:", food_name)
        print("Quantity:", quantity)
        print("Price:", price)
        print("Amount:", total)

        # Store order for repeat option

        self.order_history = [(food_id, quantity)]

        bill = input("\nDo you want to calculate bill? (y/n): ")

        if bill.lower() == "y":

            self.calculate_bill(food_name, price, quantity)

        else:

            print("Order Cancelled!")

    def calculate_bill(self, food_name, price, quantity):

        total = price * quantity

        if total > 500:

            delivery_charges = 0

        else:

            delivery_charges = 50

        final_amount = total + delivery_charges

        print("\n" + "=" * 30)
        print("             BILL")
        print("=" * 30)

        print("Restaurant:", self.rname)
        print("Customer:", self.cname)
        print("Food:", food_name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Amount:", total)
        print("Delivery Charges:", delivery_charges)
        print("Total Amount:", final_amount)

        print("=" * 30)


# ---------------- MAIN PROGRAM ----------------


print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")

cname = input("Enter Customer Name: ")
address = input("Enter Customer Address: ")
rname = input("Enter Restaurant Name: ")
obj = order(cname, address, rname)
while True:
    print("\n========== MENU ==========")
    print("1. Customer Info")
    print("2. Restaurant Details")
    print("3. Order")
    print("4. Generate Bill")
    print("5. Exit")
    print("==========================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.dcd()
    elif choice == 2:
        obj.drd()
        obj.display_menu()
    elif choice == 3:
        obj.take_order()
    elif choice == 4:
        print("\nBill is generated when you choose 'y'")
        print("for calculating bill after placing an order.")
    elif choice == 5:
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice! Please try again.")
