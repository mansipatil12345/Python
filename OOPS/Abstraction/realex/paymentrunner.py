from upi import upi 
from gpay import gpay
u = upi()
g = gpay()
u.pay(1000)
g.pay(500)

choice = input("Enter yr choice: upi gpay ")
if choice=='upi':
    amount = int(input("Enter yr amount to pay: "))
    payment_choice = upi()
elif choice=='gpay':
    amount = int(input("Enter yr amount to pay: "))
    payment_choice = gpay()
else:
    print("invalid choice!")

payment_choice.pay(amount)