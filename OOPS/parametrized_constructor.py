# class student:
#     pass
# #default con
#     def __init__(self):
#         print("called while creating object of class!")
# #parametrized constructor--->instance var intialize
#     def __init__(self,usname,usage):
#         self.name = usname
#         self.age = usage

# #will give error by default constructor 
# # s.student()

# # s= student("ram",90)
# # print(s.name,s.age)

# # s1 = student("sita",70)
# # print(s1.name,s1.age)

# #another better option to create object and storing it is list
# All_students =[student("ram",90),student("sita",80),student("ramesh",60)]

# #names
# #return memory location
# print(All_students) 

# #loop
# for s in All_students:
#     print(s.name) #prints name

# for s in All_students:
#     print(s.marks) #prints marks




#1
# class product:
#     brand = "HNM"

#     def __init__ (self,product,price,Qty):
#         self.product= product
#         self.price = price
#         self.Qty = Qty

# Mall = [product("Jeans",1200,1),product("TShirt",400,2),product("Shoes",800,1),product("Shirt",2000,4),product("Jacket",1000,1)]

# sum=0
# for m in Mall:
#     print(m.product)
#     print(m.price)
#     print(m.Qty)
#     total_amount=m.Qty*m.price
#     sum+=total_amount
# print(f"Total is : {sum}")


# for m in Mall:
#     if(m.Qty>3):
#         print(f"{m.product} is having Quantity greater than 3")
    
    
    


