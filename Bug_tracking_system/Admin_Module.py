# ------------------------------ADMIN MODULE---------------------------------

import mysql.connector

# Establishing connection with the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="bug_tracking_system"
)


# Customer Services
def view_all_customers():

    cursor = db.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)
    customers = cursor.fetchall()

    if customers:
        print("\nAll Customers:")
        for customer in customers:
            print(f"Customer Login ID: {customer[0]}, Customer Name: {customer[2]}, Customer Age: {customer[3]}, Customer Phone: {customer[4]}, Customer Email: {customer[5]}")
    else:
        print("No customers found.")


def search_customer_by_name():

    customer_name = input("Enter the customer name you want to search: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custName = %s"
    values = (customer_name,)
    cursor.execute(query, values)
    customers = cursor.fetchall()

    if customers:
        print(f"\nCustomers with name '{customer_name}':")
        for customer in customers:
            print(f"Customer Login ID: {customer[0]}, Customer Name: {customer[2]}, Customer Age: {customer[3]}, Customer Phone: {customer[4]}, Customer Email: {customer[5]}")
    else:
        print(f"No customers found with name '{customer_name}'.")


def search_customer_by_loginId():

    cust_loginId = input("Enter customer login ID: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custLoginId = %s"
    values = (cust_loginId,)
    cursor.execute(query, values)
    customer = cursor.fetchone()

    if customer:
        print(f"\nCustomers with loginID '{cust_loginId}': ")
        print(f"\n Customer Login ID: {customer[0]}\n Customer Name: {customer[2]}\n Customer Age: {customer[3]}\n Customer Phone: {customer[4]}\n Customer Email: {customer[5]}")
    else:
        print(f"No customer found with loginID '{cust_loginId}'. ")


# Employee Services
def employee_add_new():

    empLoginId = input("Enter employee login ID: ")
    empPassword = input("Enter password: ")
    empType = input("Enter the employee type (ADMIN/EXPERT): ")
    empName = input("Enter the employee name: ")
    empPhone = input("Enter the employee phone number: ")
    empEmail = input("Enter the employee email: ")
    empStatus = input("Enter the employee status: ")

    cursor = db.cursor()

    query = "INSERT INTO employee (empLoginId, empPassword, empType, empName, empPhone, empEmail, empStatus) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (empLoginId, empPassword, empType, empName, empPhone, empEmail, empStatus)
    cursor.execute(query, values)
    db.commit()

    print("New employee is successfully added!")


def view_all_employees():

    cursor = db.cursor()
    query = "SELECT * FROM employee"
    cursor.execute(query)
    employees = cursor.fetchall()

    if employees:
        print("\nAll Employees:\n")
        for employee in employees:
            print("----------------------------------------------")
            print(f"Employee Login ID: {employee[0]}\n Employee Password: {employee[1]}\n Employee Type: {employee[2]}\n Employee Name: {employee[3]}\n Employee Phone: {employee[4]}\n Employee Email: {employee[5]}\n Employee Status: {employee[6]}")
            print("\n")
        print("----------------------------------------------")
    else:
        print("No customers found.")


def search_employee_by_name():

    employee_name = input("Enter the employee name you want to search: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empName = %s"
    values = (employee_name,)
    cursor.execute(query, values)
    employees = cursor.fetchall()

    if employees:
        print(f"Employees with name '{employee_name}':")
        for employee in employees:
            print(f" Employee Login ID: {employee[0]}\n Employee Type: {employee[2]}\n Employee Name: {employee[3]}\n Employee Phone: {employee[4]}\n Employee Email: {employee[5]}\n Employee Status: {employee[6]}")
    else:
        print(f"No employees found with name '{employee_name}'.")


def search_employee_by_loginId():

    employee_loginId = input("Enter employee login ID: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s "
    values = (employee_loginId,)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        print(f"Employee with loginID '{employee_loginId}': ")
        print(f"\n Employee Login ID: {employee[0]}\n Employee Type: {employee[2]}\n Employee Name: {employee[3]}\n Employee Phone: {employee[4]}\n Employee Email: {employee[5]}\n Employee Status: {employee[6]}")
    else:
        print(f"No customer found with loginID '{employee_loginId}'. ")


def search_employee_by_type():

    employee_type = input("Enter the employee type you want to search (ADMIN/EXPERT): ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empType = %s"
    values = (employee_type,)
    cursor.execute(query, values)
    employees = cursor.fetchall()

    if employees:
        print(f"Employees with type '{employee_type}':")
        for employee in employees:
            print(f" Employee Login ID: {employee[0]}\n Employee Type: {employee[2]}\n Employee Name: {employee[3]}\n Employee Phone: {employee[4]}\n Employee Email: {employee[5]}\n Employee Status: {employee[6]}")
            print("\n")
    else:
        print(f"No employees found with type '{employee_type}'.")


def employee_activate_deactivate():

    employee_login_Id = input("Enter the employee login ID you want to activate/deactivate: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s"
    values = (employee_login_Id,)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        if employee[6] == "INACTIVE":
            new_Status = "ACTIVE"
        else:
            new_Status = "INACTIVE"
        update = "UPDATE employee SET empStatus = %s WHERE empLoginId = %s"
        updated_values = (new_Status, employee_login_Id)
        cursor.execute(update, updated_values)
        db.commit()

        print(f"Status of Employee with Login ID '{employee_login_Id}' is successfully updated to '{new_Status}' from '{employee[6]}'")
    else:
        print(f"Employee with Login ID '{employee_login_Id}' not found")


def change_password():

    employee_login_Id = input("Enter the employee login ID to change its password: ")
    new_pass = input("Enter the new password:")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s"
    values = (employee_login_Id,)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        update = "UPDATE employee SET empPassword = %s WHERE empLoginId = %s"
        updated_values = (new_pass, employee_login_Id)
        cursor.execute(update, updated_values)
        db.commit()

        print(f"Password of Employee with Login ID '{employee_login_Id}' is successfully updated to '{new_pass}' from '{employee[1]}'")
    else:
        print(f"Employee with Login ID '{employee_login_Id}' not found")


# Bug Services
def view_all_bugs():
    cursor = db.cursor()
    query = "SELECT * FROM bug"
    cursor.execute(query)
    bugs = cursor.fetchall()

    if bugs:
        print("All Bugs:")
        for bug in bugs:
            print(f"\n custLoginId: '{bug[2]}'\n bugStatus: '{bug[3]}'\n productName: '{bug[4]}'\n bugDesc: '{bug[5]}'")
            print("\n")
    else:
        print("No bugs found.")


def search_bug_by_bugId():

    bug_Id = input("Enter Bug ID: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugId = %s "
    values = (bug_Id,)
    cursor.execute(query, values)
    bug = cursor.fetchone()

    if bug:
        print(f"Bug with bugID '{bug_Id}': ")
        print(f"\n custLoginId: '{bug[2]}'\n bugStatus: '{bug[3]}'\n productName: '{bug[4]}'\n bugDesc: '{bug[5]}'")
    else:
        print(f"No bug found with bugID '{bug_Id}'. ")


def search_bug_by_status():

    bug_status = input("Enter the bug status you want to search (New Bug/Assigned/Solved): ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugStatus = %s"
    values = (bug_status,)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs with status '{bug_status}':")
        for bug in bugs:
            print(f"\n custLoginId: '{bug[2]}'\n bugStatus: '{bug[3]}'\n productName: '{bug[4]}'\n bugDesc: '{bug[5]}'")
            print("\n")
    else:
        print(f"No bugs found with status '{bug_status}'.")


def search_bug_by_custLoginId():

    cust_loginId = input("Enter customer login ID to search the bug: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE custLoginId = %s "
    values = (cust_loginId,)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs with Customer Login ID '{cust_loginId}': ")
        for bug in bugs:
            print(f"\n custLoginId: '{bug[2]}'\n bugStatus: '{bug[3]}'\n productName: '{bug[4]}'\n bugDesc: '{bug[5]}'")
            print("\n")
    else:
        print(f"No bugs found with custLoginID '{cust_loginId}'. ")


def assign_bug_to_expert():
    bug_id = input("Enter the bug ID to assign: ")
    expert_login_id = input("Enter the expert login ID to assign: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugId = %s"
    values = (bug_id,)
    cursor.execute(query, values)
    bug = cursor.fetchone()

    if bug:
        update_query = "UPDATE bug SET bugStatus = 'Assigned', expertAssignedDate = NOW(), expertLoginId = %s WHERE bugId = %s"
        update_values = (expert_login_id, bug_id)
        cursor.execute(update_query, update_values)
        db.commit()
        print(f"Bug with ID '{bug_id}' has been assigned to expert with login ID '{expert_login_id}'.")
    else:
        print(f"No bug found with ID '{bug_id}'.")


# ***************************************** MAIN MENU *****************************************
def admin_module_menu():
    print("\n+------------------------------------------------ADMIN MODULE-------------------------------------------------+")
    print("|1. Customer Services - Manage Services (View, Search)                                                        |")
    print("|2. Employee Services - Manage Employee (Admin & Expert types)(Add, View, Search, Edit, Activate/Deactivate)  |")
    print("|3. Bug Services - Manage Bug(View, Search, AssignBugToExpert)                                                |")
    print("|4. Exit                                                                                                      |")
    print("+-------------------------------------------------------------------------------------------------------------+")

    choice = int(input("\nEnter your choice:"))

    if choice == 1:
        print("\n1. Customer: View All")
        print("2. Customer: Search - by Customer Name")
        print("3. Customer: Search - by Customer Login ID")

        choice1 = int(input("\nEnter your choice(1-3):"))

        if choice1 == 1:
            view_all_customers()
        elif choice1 == 2:
            search_customer_by_name()
        elif choice1 == 3:
            search_customer_by_loginId()
        else:
            print("Invalid Choice!!!")

    elif choice == 2:
        print("\n1. Employee: Add New (Admin or Expert)")
        print("2. Employee: View All")
        print("3. Employee: Search - by Employee Name")
        print("4. Employee: Search - by Employee Login ID")
        print("5. Employee: Search - by Employee Type")
        print("6. Employee: Activate or Deactivate")
        print("7. Employee: Change Password")

        choice2 = int(input("\nEnter your choice(1-7):"))

        if choice2 == 1:
            employee_add_new()
        elif choice2 == 2:
            view_all_employees()
        elif choice2 == 3:
            search_employee_by_name()
        elif choice2 == 4:
            search_employee_by_loginId()
        elif choice2 == 5:
            search_employee_by_type()
        elif choice2 == 6:
            employee_activate_deactivate()
        elif choice2 == 7:
            change_password()
        else:
            print("Invalid Choice!!!")

    elif choice == 3:
        print("\n1. Bug: View All")
        print("2. Bug: Search by bugId")
        print("3. Bug: Search by status")
        print("4. Bug: Search by custLoginId")
        print("5. Bug: Assign to Expert")
        print("6. Logout")

        choice3 = int(input("\nEnter your choice (1-6):"))

        if choice3 == 1:
            view_all_bugs()
        elif choice3 == 2:
            search_bug_by_bugId()
        elif choice3 == 3:
            search_bug_by_status()
        elif choice3 == 4:
            search_bug_by_custLoginId()
        elif choice3 == 5:
            assign_bug_to_expert()
        elif choice3 == 6:
            print("Logging out...")
            return
        else:
            print("Invalid choice.")

    elif choice == 4:
        print("Successfully Exited From Admin Module")
        return

    else:
        print("Invalid Choice")


# Calling the admin module menu
admin_module_menu()

# Closing the database connection
db.close()
