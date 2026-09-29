#inbuild functions : math random datetime 
# from math import *

# print(pow(2,5))
# print(ceil(90.99)) #91
# print(floor(90.99))#90
# print(pi)
# print(sum([10,20]))

# from random import *
# #randint-> provide length for otp
# otp = randint(1111,9999)
# print(otp)

# #use of random function
# import random as r

# print(r,uniform(10,20))
# print(r,randrange(1,20,2))
# print(r,randrange(0,20,2))

# names=["ram","ramu","ramesh"]
# print(r.choice[names])

# food = ["pizza","noodles","sandwich","burger"]
# print(r.choices(food,k=2))


#use of datetime
# import datetime as d

# #current time stamp
# current = d.datetime.now()
# print(current)

# #only date
# date = d.datetime.now()
# print(date.date())
# print(date.year,date.month,date.day)
# print(date.hour,date.minute,date.second)


#design a function - user take username and password -> if correct - login successful
#wrong - in cred --> otp login by otp : y/n?
# if yes (y) otp send -> otp receive --> compare --> match : login success
#otp mismatch :invalid otp


# from random import *
# def validation(user_ip,pass_ip,otp_in):
#     username = "Mansi"
#     password = "mansi@123"
#     if(username==user_ip and password==pass_ip):
#         print("LOGIN SUCESSFULLY") 
#     else:
#         print("login through otp")
#         otp = int(input("Enter the otp: "))
#         if(otp==otp_in):
#             print("LOGIN SUCCESSFULLY")
#         else:
#             print("Enter valid otp")

# otp_in= randint(1,9)
# user_in = input("Enter the username: ")
# pw_in = input("Enter the password: ")
# validation(user_in,pw_in,otp_in)