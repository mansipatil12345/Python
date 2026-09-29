import sqlite3;

#all methods from db is stored in conn
conn = sqlite3.connect("python46.db")
print("db created")

#entire refrence is stored 
cursor = conn.cursor()

#call execute -> table create
cursor.execute("""
    create table if not exists student(
        id INTEGER primary key,
        name TEXT not null,
        age INTEGER
    )
    """)
print("table created!")

#insert op-static one 
# cursor.execute("INSERT INTO student(id,name,age) VALUES(?,?,?)",(1,'Ram',23))
# conn.commit()
# print("data created")


#by user input-dynamic
# id=int(input("Enter the id: "))
# name=input("Enter the name: ")
# age=int(input("Enter the age: "))
# cursor.execute("INSERT INTO student(id,name,age) VALUES(?,?,?)",(id,name,age))
# conn.commit()
# print("data created")


#add multiple records
#way 1-> manual process
#single-> tuple , multiple->list input dete time
# students=[(4,"Gopi",34),(5,"Siya",47)]
# cursor.executemany("INSERT INTO student(id,name,age) VALUES(?,?,?)",students)
# conn.commit()
# print("All data added!")


#executemany works faster than execute 
#when multiple inputs are passed throguh execute many data is passed faster companritively takinga loop and then doing it through execute for each data

#way2-> 3 students at a time---> 
# ip = int(input("Enter how many students do u want to add?"))
# for i in range(ip):
#     id=int(input("Enter the id: "))
#     name=input("Enter the name: ")
#     age=int(input("Enter the age: "))
#     cursor.execute("INSERT INTO student(id,name,age) VALUES(?,?,?)",(id,name,age))
#     conn.commit()
#     print(f"{i+1} data created")


#
# std=[]
# ip = int(input("Enter how many students do u want to add?"))
# for i in range(ip):
#     id=int(input("Enter the id: "))
#     name=input("Enter the name: ")
#     age=int(input("Enter the age: "))
#     student = (id,name,age)
#     std.append(student)
# cursor.executemany("INSERT INTO student(id,name,age) VALUES(?,?,?)",std)
# conn.commit()
# print("Data added")

#Display
# cursor.execute("select * from student")
# rows = cursor.fetchall()
# print(rows)
# for row in rows:
#     print(row[1]) #every tuple has (0-> id, 1-> name,2->age) so to get any particular data pass the index
#     print(f"{row[1]} {row[2]}") # name with their age
#without loop row ->[(),()]
#with loop row one by one print--->value


#particular : select * from student where column = value;
# cursor.execute("select * from student where id=?",(4,)) #tuple cannot have single value hence comma must be provided
# row = cursor.fetchone()
# print(row)

    
#update
# newid = int(input("Enter the id you want to update: "))
# newname=input("Enter the new name: ")
# newage = input("Enter the new age: ")
# cursor.execute("""
#     UPDATE student
#     SET name=?,age=?
#     WHERE id=?;
# """,(newname,newage,newid))     #execute have two arg only and also values in tuple should be according to pattern of placeholders
# conn.commit()
# print("Data updated")


# delete
# newid = int(input("Enter the id you want to delete: "))
# cursor.execute("""
#     DELETE FROM student 
#     WHERE id = ?;
# """,(newid,))     
# conn.commit()
# print("Data Deleted!")

#sorting
# order = input("Enter the order in which you want to sort (ASC/DESC): ")
# col = input("Enter the column name according to which you want to sort: ")
# cursor.execute(f"SELECT * FROM student ORDER BY {col} {order};")   
# #you cannot pass ? this placeholer for val is want to pass col using string {} no need to pass tuple 
# #Use ? for DATA/VALUES. Use a string/f-string for SQL structure such as column names or keywords.
# # for select use fetchall and run a loop to print all rows
# rows  = cursor.fetchall()
# for row in rows:
#     print(row)
# print("Data sorted!")


    








