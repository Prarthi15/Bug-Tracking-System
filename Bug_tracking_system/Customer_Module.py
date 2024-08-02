# --------------------------CUSTOMER MODULE------------------------------

import mysql.connector

# Establishing connection with the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="bug_tracking_system"
)


def create_account():
    print("\n______________________CREATE ACCOUNT______________________")
    custLoginId = input("\n1Enter a unique customer login ID: ")
    custPassword = input("Enter a password: ")
    custName = input("Enter the customer name: ")
    custAge = int(input("Enter the customer age: "))
    custPhone = input("Enter the customer phone number: ")
    custEmail = input("Enter the customer email: ")

    cursor = db.cursor()
    query = "INSERT INTO customer (custLoginId, custPassword, custName, custAge, custPhone, custEmail) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (custLoginId, custPassword, custName, custAge, custPhone, custEmail)
    cursor.execute(query, values)
    db.commit()

    print("\nCUSTOMER ACCOUNT CREATED SUCCESSFULLY!!!!!")


def update_account():
    print("\n______________________UPDATE ACCOUNT______________________\n")
    print("+---------------------+")
    print("|1. Update Password   |")
    print("+---------------------+")
    print("|2. Update Name       |")
    print("+---------------------+")
    print("|3. Update Age        |")
    print("+---------------------+")
    print("|4. Update Phone      |")
    print("+---------------------+")
    print("|5. Update Email ID   |")
    print("+---------------------+")
    print("|6. Update All        |")
    print("+---------------------+")
    print("|7. Exit              |")
    print("+---------------------+")

    cursor = db.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)
    customers = cursor.fetchall()

    choice = input("\nEnter your choice(1-7):")

    if customers:
        if choice == '1':
            print("\n*********** UPDATE PASSWORD ***********\n")
            custLoginId = input("Enter the customer Login ID:")
            old_custPassword = input("Enter the old customer password:")
            new_custPassword = input("Enter the new customer password:")
            update = "UPDATE customer SET custPassword = %s WHERE custLoginId = %s AND custPassword = %s"

            values = (new_custPassword, custLoginId, old_custPassword)
            cursor.execute(update, values)
            db.commit()
            print("\nUPDATION SUCCESSFUL!!!!!")
        elif choice == '2':
            print("\n*********** UPDATE NAME ***********\n")
            custLoginId = input("Enter the customer Login ID:")
            new_name = input("Enter new customer name:")

            update = "UPDATE customer SET custName = %s WHERE custLoginId = %s"
            values = (new_name, custLoginId)
            cursor.execute(update, values)
            db.commit()
            print("\nUPDATION SUCCESSFUL!!!!!")
        elif choice == '3':
            print("\n*********** UPDATE AGE ***********\n")
            custLoginId = input("Enter the customer Login ID:")
            new_age = input("Enter new customer age:")

            update = "UPDATE customer SET custAge = %s WHERE custLoginId = %s"
            values = (new_age, custLoginId)
            cursor.execute(update, values)
            db.commit()
            print("\nUPDATION SUCCESSFUL!!!!!")
        elif choice == '4':
            print("\n*********** UPDATE PHONE ***********\n")
            custLoginId = input("Enter the customer Login ID:")
            new_phone = input("Enter new customer Phone number:")
            update = "UPDATE customer SET custPhone = %s WHERE custLoginId = %s"
            values = (new_phone, custLoginId)
            cursor.execute(update, values)
            db.commit()
            print("\nUPDATION SUCCESSFUL!!!!!")
        elif choice == '5':
            print("\n*********** UPDATE EMAIL ID ***********\n")
            custLoginId = input("Enter the customer Login ID:")
            new_email = input("Enter new customer Email ID:")

            update = "UPDATE customer SET custEmail5 = %s WHERE custLoginId = %s"
            values = (new_email, custLoginId)
            cursor.execute(update, values)
            db.commit()
            print("\nUPDATION SUCCESSFUL!!!!!")
        elif choice == '6':
            print("\n*********** UPDATE ALL ***********\n")
            custLoginId = input("Enter the customer Login ID:")
            new_custPassword = input("Enter the new customer password:")
            new_name = input("Enter new customer name:")
            new_age = input("Enter new customer age:")
            new_phone = input("Enter new customer Phone number:")
            new_email = input("Enter new customer Email ID:")

            update = "UPDATE customer SET custPassword = %s, custName = %s, custAge = %s, custPhone = %s, custEmail = %s WHERE custLoginId = %s"
            values = (new_custPassword, new_name, new_age, new_phone, new_email, custLoginId)
            cursor.execute(update, values)
            db.commit()
            print("UPDATION SUCCESSFUL!!!!!")
        elif choice == '7':
            print("EXIT........")
            return

    else:
        print("NO CUSTOMER FOUND!!!")


def post_new_bug():
    print("\n______________________POST NEW BUG______________________")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    custLoginId = input("\nEnter the customer LoginId:")
    productName = input("Enter the Product Name: ")
    bugDesc = input("Enter description of the bug:")

    query = "INSERT INTO bug(custLoginId, productName, bugDesc) VALUES(%s, %s, %s)"
    values = (custLoginId, productName, bugDesc)
    cursor.execute(query, values)
    print("\nNEW BUG POSTED SUCCESSFULLY!!!")

    db.commit()
    db.close()


def view_all_bugs():
    print("\n______________________VIEW ALL BUGS______________________")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prompt for the account's login ID
    loginid = input("\nEnter the customer LoginId :")

    # Execute the SQL select query
    query = "SELECT * FROM bug WHERE custLoginId = %s"
    values = (loginid,)
    cursor.execute(query, values)

    # Fetch all the bugs
    bugs = cursor.fetchall()

    print("\n")
    print("-----------------------------------------")
    # Print the bugs
    for bug in bugs:
        print("Bug ID              :", bug[0])
        print("Posting Date        :", bug[1])
        print("Customer Login ID   :", bug[2])
        print("Bug Status          :", bug[3])
        print("Product Name        :", bug[4])
        print("Bug Description     :", bug[5])
        print("Expert Assigned Date:", bug[6])
        print("Expert Login ID     :", bug[7])
        print("Bug Solved Date     :", bug[8])
        print("Solution            :", bug[9])
        print("-----------------------------------------")
    db.commit()
    db.close()


def bugs_status():
    print("\n______________________BUGS STATUS______________________")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    status = input("\nBug status to search (New Bug/Solved/Assigned): ")

    # Execute the SQL select query
    query = "SELECT * FROM bug where bugStatus = %s"
    value = (status, )
    cursor.execute(query, value)

    # Fetch all the bugs
    bugs = cursor.fetchall()

    print("\n")
    print("-----------------------------------------")

    # Print the bugs
    for bug in bugs:
        print("Bug ID         :", bug[0])
        print("Posting Date   :", bug[1])
        print("Product Name   :", bug[4])
        print("Bug Description:", bug[5])
        print("-----------------------------------------")

    # Close the cursor and database connection
    cursor.close()
    db.commit()
    db.close()


def view_bug_solution():
    print("\n______________________BUGS SOLUTION______________________")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prompt for the account's login ID and the status to search for
    loginid = input("\nEnter the LoginId: ")
    bug_id = int(input("Enter the bug ID to view the solution: "))

    # Execute the SQL select query
    query = "SELECT solution FROM bug WHERE bugId = %s and custLoginId='%s'"
    values = (bug_id, loginid)
    cursor.execute(query, values)
    bug_solution = cursor.fetchone()

    if bug_solution:
        print("Bug Solution:", bug_solution[0])
    else:
        print("BUG SOLUTION NOT FOUND!!!.")

    db.commit()
    db.close()


def change_password():
    print("\n______________________CHANGE PASSWORD______________________")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    loginId = input("\nEnter the LoginId:")
    old_custPassword = input("Enter the Old Password:")
    new_custPassword = input("Enter the New Password:")
    query = "UPDATE customer SET custPassword = %s WHERE custLoginId = %s AND custPassword = %s"
    value = (new_custPassword, loginId, old_custPassword)
    cursor.execute(query, value)
    print("\nPASSWORD CHANGED!!!!")

    db.commit()
    db.close()


# ***************************************** MAIN MENU *****************************************
def main_menu():
    print("\n+---------CUSTOMER MODULE---------+")
    print("|1. Create Account                |")
    print("|2. Update Account                |")
    print("|3. Post New Bug                  |")
    print("|4. View All Bugs                 |")
    print("|5. Search Bugs based on status   |")
    print("|6. View Bug Solution             |")
    print("|7. Change Password               |")
    print("|8. Exit                          |")
    print("+---------------------------------+")

    choice = int(input("\nEnter your choice(1-8):"))
    if choice == 1:
        create_account()
    elif choice == 2:
        update_account()
    elif choice == 3:
        post_new_bug()
    elif choice == 4:
        view_all_bugs()
    elif choice == 5:
        bugs_status()
    elif choice == 6:
        view_bug_solution()
    elif choice == 7:
        change_password()
    elif choice == 8:
        print("Exit!!!")

    else:
        print("INVALID CHOICE!!!!")


main_menu()
