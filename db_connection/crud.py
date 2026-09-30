from dbconn import db_conn

#setting the connection
conn,cursor = db_conn()

#CREATE TABLE
def create_table():
    print("------------------------------------------------------------------------------------")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS product(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            qty INT CHECK (qty>0),
            price DECIMAL(10,2),
            brand TEXT NOT NULL,
            color TEXT
        );
    """)
    print("TABLE PRODUCT CREATED")
    print("------------------------------------------------------------------------------------")



#INSERT
def insert():
    products=[]
    ip = int(input("Enter how many products u want to add? "))
    count = 0
    for i in range(ip):
        name = input("Enter the name: ")
        qty = int(input("Enter the qty of the product: "))
        price = int(input("Enter the prices of the product: "))
        brand = input("Enter the brand:  ")
        color = input("Enter the color:  ")
        products.append((name,qty,price,brand,color))
        count+=1
    cursor.executemany("INSERT INTO product(name,qty,price,brand,color) VALUES(?,?,?,?,?)",products)
    conn.commit()
    print(f"DATA {count} ADDED !")
# insert()



#DISPLAY:
def display():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    for row in rows:
        print("|----------------------------------------------------------------------------------------------------------------|")
        print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
        print("|----------------------------------------------------------------------------------------------------------------|")
# display()

#SEARCH:
def search():
    while True:
        print("Enter the choice according to which you want to search : ")
        print("1.ID")
        print("2.Name")
        print("3.Price")
        print("4.Exit")
        choice = int(input("Enter the choice: "))
        match choice:
            case 1:
                flag = False
                pid = int(input("Enter the id you want to search: "))
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                for row in rows:
                    if row[0]==pid:
                        print(f"ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR: {row[5]}")
                        flag=True
                        break
                if(flag==False):
                    print("Product with this id not available!")

            case 2:
                flag = False
                name = input("Enter the name you want to search: ")
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                for row in rows:
                    if row[1]==name:
                        print(f"ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
                        flag=True
                        break
                if(flag==False):
                    print("Product with this name not available!")

            case 3:
                flag = False
                price = int(input("Enter the price you want to search for the product: "))
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                for row in rows:
                    if row[3]==price:
                        print(f"ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
                        flag=True
                        break
                if(flag==False):
                    print("Product with this price not available!")
            case 4:
                print("Exiting....")
                break

            case _:
                print("Invalid choice!")
# search()


# TOTOAL PRODUCT PRICE
def total_product_price():
    cursor.execute("SELECT sum(price) AS total_product_price FROM product;")
    row = cursor.fetchone()
    print(f"The total product price is {row[0]}") # to print with out op is (x,) so print row[0]-> x
# total_product_price()



# SORTING
def sort_products():
    print("Enter the choice on which you want to sort the products: ")
    print("1.name")
    print("2.price")
    choice = int(input("Enter the choice: "))

    if (choice==1):
        order = input("Enter the order in which you want to sort (A-Z /Z-A): ")
        if(order=="A-Z"):
            cursor.execute("SELECT * FROM PRODUCT ORDER BY name ASC")
            rows = cursor.fetchall()
            for row in rows:
                print("|----------------------------------------------------------------------------------------------------------------|")
                print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
                print("|----------------------------------------------------------------------------------------------------------------|")
        else:
            cursor.execute("SELECT * FROM PRODUCT ORDER BY name ASC")
            rows = cursor.fetchall()
            for row in rows:
                print("|----------------------------------------------------------------------------------------------------------------|")
                print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
                print("|----------------------------------------------------------------------------------------------------------------|")
    elif(choice==2):
        order = int(input("Enter the order in which you want to sort (1.low-to-high /2. high-to-low): "))
        if(order==1):
            cursor.execute("SELECT * FROM PRODUCT ORDER BY price ASC")
            rows = cursor.fetchall()
            for row in rows:
                print("|----------------------------------------------------------------------------------------------------------------|")
                print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
                print("|----------------------------------------------------------------------------------------------------------------|")
        else:
            cursor.execute("SELECT * FROM PRODUCT ORDER BY price DESC")
            rows = cursor.fetchall()
            for row in rows:
                print("|----------------------------------------------------------------------------------------------------------------|")
                print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
                print("|----------------------------------------------------------------------------------------------------------------|")
    else:
        print("Enter valid choice!")
# sort_products()


# PRODUCT WITH NO COLOR
def display_nocolor_products():
    cursor.execute("SELECT * FROM product WHERE color IS NULL;")
    rows = cursor.fetchall()
    if len(rows)==0:
        print("No product found with no color")
    else:
        for row in rows:
            print("|----------------------------------------------------------------------------------------------------------------|")
            print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
            print("|----------------------------------------------------------------------------------------------------------------|")
# display_nocolor_products()


# ERROR 
# cursor.execute("SELECT typeof(color) FROM product;")
# rows = cursor.fetchall()
# print(rows)

# cursor.execute("UPDATE product SET color = NULL WHERE color = 'NULL';")
# conn.commit()

# cursor.execute("SELECT typeof(color) FROM product;")
# rows = cursor.fetchall()
# print(rows)


#UPDATE PRODUCT
def update_product():
    while True:
        print("Enter the choice what you want to update \n1.Name\n2.Brand\n3.Id\n4.Exit")
        choice = int(input("Enter the choice: "))
        match choice:
            case 1:
                flag = False
                name = input("Enter the name for you want updation: ")
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                for row in rows:
                    if(row[1]==name):
                        pname= input("Enter the updated name: ")
                        nqty = int(input("Enter the new quantity: "))
                        nprice = int(input("Enter the updated price: "))
                        nbrand = input("Enter the updated brand: ")
                        ncolor = input("Enter the new color: ")
                        cursor.execute("UPDATE product SET name=?,qty=?,price=?,brand=?,color=? WHERE name = ?;",(pname,nqty,nprice,nbrand,ncolor,name))
                        conn.commit()
                        flag = True
                        break
                if(flag==False):
                    print("No records found for this name!")
            case 2:
                flag = False
                ubrand = input("Enter the brand for you want updation: ")
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                for row in rows:
                    if(row[4]==ubrand):
                        pname= input("Enter the updated name: ")
                        nqty = int(input("Enter the new quantity: "))
                        nprice = int(input("Enter the updated price: "))
                        nbrand = input("Enter the updated brand: ")
                        ncolor = input("Enter the new color: ")
                        cursor.execute("UPDATE product SET name=?,qty=?,price=?,brand=?,color=? WHERE brand = ?;",(pname,nqty,nprice,nbrand,ncolor,ubrand))
                        conn.commit()
                        flag = True
                        break
                if(flag==False):
                    print("No records found for this brand!")

            case 3:
                flag = False
                uid = int(input("Enter the id for you want updation: "))
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                for row in rows:
                    if(row[0]==uid):
                        pname= input("Enter the updated name: ")
                        nqty = int(input("Enter the new quantity: "))
                        nprice = int(input("Enter the updated price: "))
                        nbrand = input("Enter the updated brand: ")
                        ncolor = input("Enter the new color: ")
                        cursor.execute("UPDATE product SET name=?,qty=?,price=?,brand=?,color=? WHERE id = ?;",(pname,nqty,nprice,nbrand,ncolor,uid))
                        conn.commit()
                        flag = True
                        break
                if(flag==False):
                    print("No records found for this id!")
            case 4:
                print("Exiting...")
                break
            case _:
                print("Invalid Choice!")
# update_product()


#DELETE
def delete_product():
    print("Enter the choice what you want to delete \n1.Delete any perticular row\n2.Delete all")
    choice = int(input("Enter the choice: "))
    if(choice==1):
        flag = False
        pid = int(input("Enter the id to delete: "))
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        for row in rows:
            if row[0]==pid:
                cursor.execute("DELETE FROM product WHERE id=?",(pid,))
                conn.commit()
                print(f"Data {pid} deleted!")
                flag = True
                break
        if flag==False:
            print("No records found!")
    elif(choice==2):
        cursor.execute("DELETE FROM product")
        conn.commit()
        print("All Data deleted!")
    else:
        print("Enter valid choice")
# delete_product()


def costliest_product():
    cursor.execute("SELECT * FROM product ORDER BY price DESC LIMIT 1;")
    row = cursor.fetchone()
    print("|------------------------------COSTILIEST PRODUCT----------------------------------------------------------|")
    print(f" ID : {row[0]} |  NAME : {row[1]}  | QTY: {row[2]}  | PRICE: {row[3]} |  BRAND: {row[4]} | COLOR:{row[5]}")
    print("|----------------------------------------------------------------------------------------------------------------|")
# costliest_product()


def product_mrt_5():
    cursor.execute("SELECT name, qty FROM product WHERE qty>5;")
    rows = cursor.fetchall()
    for row in rows:
        print("|------------------------------PRODUCT MORE THAN 5----------------------------------------------------------|")
        print(f"NAME : {row[0]}  | QTY: {row[1]}")
        print("|----------------------------------------------------------------------------------------------------------------|")
# product_mrt_5()
# if select has  * then printing me row has index 1 and 2 considering id as 0 
# but if select has name qty then name is assigned 0 and qty is assigned 1 since result is in tuple form so tuple starts from 0


                



