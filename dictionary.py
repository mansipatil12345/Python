# x={}
# print(x,type(x))

# #add
# x["id"]=101
# x["name"]="ram"
# x[101]="hello" #nay type of key can be there 
# print(x)

# #value : dict_name["id"]
# print(x["name"]) 

# #update dict_name["id"]= newvalue
# x["name"]="sita"
# print(x)


#methods

# stud={
#     "rollno":101,
#     "name":"ram",
#     "city":"pune",
#     "marks":90.89
# }

# print(stud)

# #only keys
# print(stud.keys())

# #only values
# print(stud.values())

# #k:V-> returns value in format of tuples (('k','v'))
# print(stud.items())


#loop
# stud={
#     "rollno":101,
#     "name":"ram",
#     "city":"pune",
#     "marks":90.89
# }

# #return only key
# for key in stud:
#     print(key)

# #return only values:
# for value in stud.values():
#     print(value)

# #return key and value
# for k,v in stud.items():
#     print(f"{k}:{v}")


#more methods
#update -> if key present then updates with new value if not then adds that key value pair
# stud={
#     "rollno":101,
#     "name":"ram",
#     "city":"pune",
#     "marks":90.89
# }

# stud.update({"marks":100})
# stud.update({"sub":"python"})
# print(stud)


#remove methods
#pop([key]) -> return key and returns value
# print(stud.pop("sub")) #removes the key and return its value
# print(stud)
# print(stud.popitem()) #removes that particular key value pair(last)
# print(stud)
# del stud["city"] 
# print(stud)
# print(stud.clear()) #clears whole dict
# print(stud)


# stud={
#     "rollno":101,
#     "name":"ram",
#     "city":"pune",
#     "marks":(90,99,100),
#     "sub":["java","python","html"],
#     "address":{
#         "city":"pune",
#         "state":"maharashtra",
#         "country":"india",
#         "pincode":444000
#     }
# }

# print(stud["address"]["country"])
# print(stud["sub"][1])
# print(stud["marks"][0]+stud["marks"][1])

#hw1

#print in this format
# Rollno : 101
# name: ram
# subjects marks
# java    90
# python  99
# html    100
# my address is pune, maha,india,4400



# stud={
#     "rollno":101,
#     "name":"ram",
#     "city":"pune",
#     "marks":(90,99,100),
#     "sub":["java","pyth","html"],
#     "address":{
#         "city":"pune",
#         "state":"maharashtra",
#         "country":"india",
#         "pincode":444000
#     }
# }

# print("----------------------MY INFO-------------------------------------------------------------------")
# print(f"RollNo:      |       {stud["rollno"]}")
# print(f"Name:        |       {stud["name"]}")
# subjects = stud["sub"]
# marks = stud["marks"]
# print(f"Subject:     |       Marks")
# for i in range(len(subjects)):
#     print(f"{subjects[i]}:        |       {marks[i]}")
# address = stud["address"]
# print(f"My address is {address["city"]},{address["state"]},{address["country"]},{address["pincode"]}")
# print("--------------------------------------------------------------------------------------------------")


#hw2
# name of sub in where ram scored highest marks (dynamic) using loops op-> html 100

# print marksheet of ram (follow above format)
# subject     marks
# java        90
# pyhton      99
# html        100
# total       ?
# per         ?


# stud={
#     "rollno":101,
#     "name":"ram",
#     "city":"pune",
#     "marks":(90,99,100),
#     "sub":["java","pyth","html"],
#     "address":{
#         "city":"pune",
#         "state":"maharashtra",
#         "country":"india",
#         "pincode":444000
#     }
# }



# print("----------------------MARKSHEET-------------------------------------------------------------------")
# print(f"RollNo:      |       {stud["rollno"]}")
# print(f"Name:        |       {stud["name"]}")
# subjects = stud["sub"]
# marks = stud["marks"]
# max=0
# print(f"Subject:     |       Marks")
# for i in range(len(subjects)):
#     print(f"{subjects[i]}:        |       {marks[i]}")
# for i in range(len(subjects)):
#     if(marks[i]>max):
#         max=marks[i]
#         maxind = i
# print(f"Highest marks scored in sub:")
# print(f"{subjects[maxind]}         |       {max}")
# total=0
# for i in marks:
#     total+=i
# print(f"Total        |       {total}")
# percent=(total/len(marks))*100
# print(f"Percent      |       {percent}")
# print("--------------------------------------------------------------------------------------------------")







            
            

