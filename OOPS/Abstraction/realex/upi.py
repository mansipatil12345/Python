from payment import payment
class upi(payment):
    def pay(self,amount):
        print(f"{amount} pay by UPI!")