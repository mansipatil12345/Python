# handle specific error & return predefined error msg
# print("Program start")
# exception handling : try ----> error causing state : except --> type error user msg
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)
# print("end ")


#handle specific multiple errors & u can return predefined as well as custom msg
# print("Program start")
# try:
#     a = int(input("Enter divisor"))
#     b = int(input("Enter the divient"))
#     print(b/a)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError :
#     print("enter nos only!")
# print("end ")

#combine multiple errors instead of write so many except &return one common msg
# try:
#     a = int(input("Enter division"))
#     b = int(input("Enter division"))
#     print(b/a)
# except(ZeroDivisionError,ValueError) :
#     print("some went wrong!")
# print("end ")

#when u dont know : which typ of exception will occur
# use parent exception to handle & return predefined msg as per which exception occurs
# try:
#     a = int(input("Enter division"))
#     b = int(input("Enter division"))
#     print(b/a)
# except Exception as e :
#     print(e)
# print("end ")


# key error 
# stud = {"name":"ram","age":90}
# print(stud["address"])
# try:
#     print(stud["address"])
# except KeyError as e:
#     print(e,"key not found!")


#Index error
# x =[10,20,30]
# try:
#     print(x[10])
# except IndexError as e:
#     print(e)

#else ------> error occur then except will excecute if not occurs then else execute 
#finally --> always execute no matters occurs or not 
# x=[10,20,30]
# try:
#     index = int(input("enter index no:   "))
#     print(x[index])
# except IndexError as e:
#     print(e)
# else:
#     print("i m else block")
# finally:
# print("i am alays execute")


#custom exception
# class MyException(Exception):
#     pass
# if(2>1):
#     raise MyException("hi i m exception")


# class pwdnotmatcherror(Exception):
#     pass
# if(123==1234):
#     print("pass matched")
# else:
#     raise pwdnotmatcherror("pwd not matched")

# class pwdnotmatcherror(Exception):
#     pass
# try:
#  if(123==1234):
#     print("pass matched")
# else:
#     raise pwdnotmatcherror("pwd not matched")

#complete codes pending one and check also