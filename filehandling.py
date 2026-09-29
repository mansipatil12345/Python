#to open new file 
# op=open("new_file",'x')
# print(op)


#we have to give the path if file is located in any subfolder
# try:
#     op=open("new_file.txt",'x')
#     print(op)
# except  FileExistsError as e:
#     print(e)


#write in created file
# try:
#     op=open("new_file.txt",'w')
#     op.write("hi i m write mode!")
#     print("data added!")
# except  FileExistsError as e:
#     print(e)

#remove previous data & add new one
# try:
#     op=open("new_file.txt",'w')
#     op.write("how r u ")
#     print("data added!")
# except  FileExistsError as e:
#     print(e)


# keep existing as it is and adds new data 
# try:
#     op=open("new_file.txt",'a')
#     op.write("how r u ")
#     print("data added!")
# except  FileExistsError as e:
#     print(e)


# try:
#     op=open("new_file.txt",'r')
#     print(op.readline()) #single line
#     op.write("how r u ")
#     print("data added!")
# except  FileExistsError as e:
#     print(e)



#remove file
#import os 
#os.remove('new_file.txt')






