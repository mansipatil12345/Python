#1
# def greet():
#     print("GE!")

# #you can call te function as many times you want
# greet()


#2
# def sq(num):
#     square = num*num
#     print(square)


# num = int(input("Enter number to find square: "))
# sq(num)

#3 with argument and with return type 
# def power(b,r):
#     pow = b**r
#     return pow
# # 1 way to print
# print(power(3,3))
# # 2 way to print
# op = power(2,3)
# print(op**2)



#4 Position argument 
# def bio(name,age):
#     print(f"name:{name},age:{age}")
# #manually
# bio("ram",20) #op is ram 20
# #user ip
# n_ip = input("Enter the name: ")
# a_ip = input("Enter your age: ")
# bio(n_ip,a_ip)
# #positional ip
# bio(age=a_ip,name=n_ip) # as it is mentioned now the data will go in proper positions agar sequence mismatch bhi hua toh


# def welcome(ins="linkcode"):
#     print(f"welcome:{ins}")
# welcome("linkcode tech")  #user ip is provided(if provide then output will print according to user input)
# welcome() #if not provided then by default one is printed


