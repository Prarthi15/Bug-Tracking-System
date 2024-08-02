import mysql.connector


def getBTSdatabase():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="password",
                                 database="bug_tracking_system")
    return db


print("\n--------------BUG TRACKING SYSTEM--------------\n")


# Employee Login
def employee_login():
    print("\n-------------EMPLOYEE LOGIN-------------")
    db = getBTSdatabase()
    empLoginId = input("\nEnter your employee login ID: ")
    empPassword = input("Enter your password: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s AND empPassword = %s"
    values = (empLoginId, empPassword)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        print("\nLOGIN SUCCESSFUL!!!!")
    else:
        print("\nINVALID EMPLOYEE LOGIN ID OR PASSWORD!!!")
        return

    if employee[2] == "ADMIN":
        # Import Admin Module
        import Admin_Module
        Admin_Module.admin_module_menu()
    elif employee[2] == "EXPERT":
        # Import Expert Module
        import Expert_Module
        Expert_Module.expert_module_main_menu()


# Customer Login
def customer_login():
    print("\n-------------CUSTOMER LOGIN-------------")
    db = getBTSdatabase()
    custLoginId = input("\nEnter your customer login ID: ")
    custPassword = input("Enter your password: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custLoginId = %s AND custPassword = %s"
    values = (custLoginId, custPassword)
    cursor.execute(query, values)
    customer = cursor.fetchone()

    if customer:
        print("\nLOGIN SUCCESSFUL!!!!")
        # Import Customer Module
        import Customer_Module
        Customer_Module.main_menu()
    else:
        print("\nINVALID EMPLOYEE LOGIN ID OR PASSWORD!!!")


# Employee Signup
def employee_signup():
    print("\n-------------EMPLOYEE SIGNUP-------------")
    db = getBTSdatabase()
    empLoginId = input("\nEnter a unique employee login ID: ")
    empPassword = input("Enter a password: ")
    empType = input("Enter the employee type (ADMIN/EXPERT): ")
    empName = input("Enter the employee name: ")
    empPhone = input("Enter the employee phone number: ")
    empEmail = input("Enter the employee email: ")

    cursor = db.cursor()
    query = "INSERT INTO employee (empLoginId, empPassword, empType, empName, empPhone, empEmail) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (empLoginId, empPassword, empType, empName, empPhone, empEmail)
    cursor.execute(query, values)
    db.commit()

    print("\nEMPLOYEE SIGNUP SUCCESSFUL!!!")


# Customer Signup
def customer_signup():
    db = getBTSdatabase()
    print("\n-------------CUSTOMER SIGNUP-------------")
    custLoginId = input("\nEnter a unique customer login ID: ")
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

    print("CUSTOMER SIGNUP SUCCESSFUL!!!")


# Main menu
def main_menu():

    print("Welcome to the Bug Tracking System!")
    print("+--------------------+")
    print("|1. Employee Login   |")
    print("+--------------------+")
    print("|2. Employee Signup  |")
    print("+--------------------+")
    print("|3. Customer Login   |")
    print("+--------------------+")
    print("|4. Customer Signup  |")
    print("+--------------------+\n")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        employee_login()
    elif choice == 2:
        employee_signup()
    elif choice == 3:
        customer_login()
    elif choice == 4:
        customer_signup()
    else:
        print("Invalid choice.")


# Calling the main menu
main_menu()

# Closing the database connection
# db.close()
