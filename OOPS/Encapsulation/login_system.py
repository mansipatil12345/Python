# from random import *
# class login_system:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password

#     def login(self):
#         username = input("Enter yr username: ")
#         while self.attempt<3:
#             password = input("Enter yr password: ")
#             if self.username == username and self.__password==password:
#                 print("login successfull")
#             else:
                        

        
#     def view_pwd(self):
#         print(self.__password)

#     def otp_generator(self):
#         send_otp = random.randint(1000,9999)
#         print(f"your otp is{send_otp}")
#         recieved_otp = int(input("Enter the otp which you reveived!"))
#         if send_otp == recieved_otp:
#             print("logged in successfully!")
#         else:
#             print("invalid otp")



# u1 = login_system("user1",1234)
# #public direct call
# # print(u1.username)
# #print(u1.__password) direct access is not allowed for private variable
# #indirect access to private var is 
# # u1.view_pwd()
# u1.login()