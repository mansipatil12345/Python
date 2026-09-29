class bankAccount:
    bankname="SBI"
    def __init__(self,name,bal):
        self.bal = bal
        self.name = name

    # insta method --> bal display
    def check_bal(self):
        print(f"Av bal is {self.bal}")

    def withdrawal(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if(amount < self.bal):
            self.bal = self.bal-amount
            print(f"amount {amount} debited succesfully")
        else:
            print("Insufficent amount")

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit:   "))
        if(amount>0):
            print("amount debited successfully")
            self.bal = self.bal + amount
        else:
            print("enter valid amount")
            
    
u1 = bankAccount("ram",20000)
u1.check_bal()
u1.withdrawal()
u1.check_bal()
u1.deposit()
u1.check_bal()

u2 = bankAccount("sita",10000)
u2.check_bal()
u2.withdrawal()
u2.check_bal()