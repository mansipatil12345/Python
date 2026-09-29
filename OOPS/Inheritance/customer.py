class customer:
    def __init__(self,cname,address):
        self.cname= cname
        self.address = address

    def dcd(self):
        print(f"The customer is {self.cname} and address of order is {self.address}")