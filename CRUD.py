student=[]
while True:
    choice = int(input("Welcome to sms!\n1.create account\n2.View details\n3.Update\n4.delete\n5.search\n6.exit\nEnter your choice: "))
    match choice:
        case 1:
            rollno=int(input("Enter your rollno:    "))
            name=input("Enter your name:    ")
            age=int(input("Enter your age:  "))
            marks=int(input("Enter your marks:  "))
            city=input("Enter your city:    ")
            student.append([rollno,name,age,marks,city])
            print("Student added Successfully!")

        case 2:
            if(len(student)==0):
                print("No records found")
            else:
                print("rollno       |    name   |   age     |   marks   |   city")
                print("--------------------------------------------------------")
                for i in student:
                    print(f"{i[0]}  |   {i[1]}  |   {i[2]}  |   {i[3]}  |   {i[4]}")
                    print("--------------------------------------------------------")

        case 3:
            id = int(input("Enter the rollno for which you want to do the edits:    "))
            flag =False
            for i in student:
                    if(i[0]==id):
                        rollno=int(input("Enter your rollno:    "))
                        i[1]=input("Enter your name:    ")
                        i[2]=int(input("Enter your age:  "))
                        i[3]=int(input("Enter your marks:  "))
                        i[4]=input("Enter your city:    ")
                        print("Updated!")
                        flag=True
            if(flag==False):
                print("No records found")

        case 4:
            id = int(input("Enter the rollno for which you want to delete:    "))
            flag =False
            for i in student:
                if(i[0]==id):
                    student.remove(i)
                    print("Deleted!")
                    flag=True
            if(flag==False):
                print("No records found")
        case 5:
            id = int(input("Enter the rollno for which you want to search:    "))
            flag=False
            for i in student:
                if(i[0]==id):
                    print("rollno       |    name   |   age     |   marks   |   city")
                    print("--------------------------------------------------------")
                    for i in student:
                        print(f"{i[0]}  |   {i[1]}  |   {i[2]}  |   {i[3]}  |   {i[4]}")
                        print("--------------------------------------------------------")

#hw
#1 search
#2 delete
#3 print top 3 stud name with marks
#4 find stu whose age below 20
#5 find stu whose age above 20
#6 find stu whose age in between 20 and 30(age ask from user )
#7 print stu name who live in mumbai and oune


#1. 
# case 5:
#     id = int(input("Enter the rollno for which you want to search: "))
#     flag = False

#     for i in student:
#         if i[0] == id:
#             print("rollno | name | age | marks | city")
#             print("-------------------------------------")
#             print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}")
#             flag = True
#             break

#     if flag == False:
#         print("No records found")


#2.

#     id = int(input("Enter the rollno for which you want to delete: "))
#     flag = False

#     for i in student:
#         if i[0] == id:
#             student.remove(i)
#             print("Deleted!")
#             flag = True
#             break

#     if flag == False:
#         print("No records found")


#3.


#4.Student below age 20
# flag = False

# for i in student:
#     if i[2] < 20:
#         print(f"Name: {i[1]}, Age: {i[2]}")
#         flag = True

# if flag == False:
#     print("No students found")

        
#5.Student above age 20
# flag = False

# for i in student:
#     if i[2] > 20:
#         print(f"Name: {i[1]}, Age: {i[2]}")
#         flag = True

# if flag == False:
#     print("No students found")


#6
# age = int(input("Enter a age: "))
# flag = False
# for i in student:
#     if i[2]>=20 and i[2]<=30:
#         print(f"Name: {i[1]}, Age: {i[2]}")
#       flag = True

# if flag == False:
#     print("No students found")


#7
# flag = False

# for i in student:
#     if i[4].lower() == "mumbai" or i[4].lower() == "pune":
#         print(i[1])
#         flag = True

# if flag == False:
#     print("No students found")


                







            

