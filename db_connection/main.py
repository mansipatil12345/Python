from dbconn import db_conn
from crud import *

#setting the connection
conn,cursor = db_conn()

create_table()

while True:

    print("\n================ PRODUCT MANAGEMENT SYSTEM ================")
    print("1. Insert Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Total Product Price")
    print("5. Sort Products")
    print("6. Display Products With No Color")
    print("7. Update Product")
    print("8. Delete Product")
    print("9. Costliest Product")
    print("10. Products With Quantity More Than 5")
    print("11. Exit")
    print("============================================================")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            insert()

        case 2:
            display()

        case 3:
            search()

        case 4:
            total_product_price()

        case 5:
            sort_products()

        case 6:
            display_nocolor_products()

        case 7:
            update_product()

        case 8:
            delete_product()

        case 9:
            costliest_product()

        case 10:
            product_mrt_5()

        case 11:
            print("Exiting Product Management System...")
            break

        case _:
            print("Invalid choice! Please enter a valid choice.")