# --------------------------EXPERT MODULE------------------------------

import mysql.connector


# Establishing connection with the MySQL database
def getBTSDatabase():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="password",
                                 database="bug_tracking_system")

    return db


def view_assigned_bugs():
    db = getBTSDatabase()
    cursor = db.cursor()

    print("\n---------------------View Assigned Bugs---------------------\n")

    query = "SELECT * FROM bug WHERE bugStatus = 'Assigned'"
    cursor.execute(query)
    bugs = cursor.fetchall()

    if bugs:
        print("Assigned Bugs:")
        print("------------------------------------------")

        for bug in bugs:
            print("Bug ID:", bug[0])
            print("Description:", bug[1])
            print("Status:", bug[2])
            print("Assigned To:", bug[3])
            print("------------------------------------------")

    else:
        print("\nNO ASSIGNED BUGS FOUND!!.")


def filter_Assigned_Bugs_based_on_status():
    db = getBTSDatabase()
    cursor = db.cursor()

    print("\n------------Filter Assigned Bugs based on status------------\n")

    # Execute the SQL select query
    query = "SELECT * FROM bug WHERE bugStatus = 'Assigned' GROUP BY bugStatus"
    cursor.execute(query)
    bugs = cursor.fetchall()

    if bugs:
        print("--------------------------------------------------------------")

        for bug in bugs:
            print("Bug ID              :", bug[0])
            print("Posting Date        :", bug[1])
            print("custLoginId         :", bug[2])
            print("Bug Satus           :", bug[3])
            print("Product name        :", bug[4])
            print("Bug description     :", bug[5])
            print("Expert Assigned date:", bug[6])
            print("Expert LoginId      :", bug[7])
            print("Bug solved date     :", bug[8])
            print("Solution            :", bug[9])
            print("--------------------------------------------------------------")

    else:
        print("NO BUGS FOUND!!!")

    db.commit()
    db.close()


def solve_the_Bug():
    db = getBTSDatabase()
    cursor = db.cursor()

    print("\n-----------------------Solve the Bug------------------------\n")

    bug_id = input("Bug Id of bug to solve:")
    bugSol = input("Solution of Bug:")

    query = "UPDATE bug SET bugStatus='solved',bugSolvedDate=NOW(),solution=%s WHERE bugId=%s"
    values = (bugSol, bug_id)
    cursor.execute(query, values)

    print("\n All the solved bugs:\n")

    query1 = "SELECT * FROM bug WHERE bugStatus='solved'"
    cursor.execute(query1)
    bugs = cursor.fetchall()

    print("--------------------------------------------------------------")

    for bug in bugs:
        print("Bug ID              :", bug[0])
        print("Posting Date        :", bug[1])
        print("custLoginId         :", bug[2])
        print("Bug Satus           :", bug[3])
        print("Product name        :", bug[4])
        print("Bug description     :", bug[5])
        print("Expert Assigned date:", bug[6])
        print("Expert LoginId      :", bug[7])
        print("Bug solved date     :", bug[8])
        print("Solution            :", bug[9])
        print("--------------------------------------------------------------")

    # Close the cursor and database connection
    db.commit()
    db.close()


def expert_Change_Password():
    db = getBTSDatabase()
    cursor = db.cursor()

    print("\n-----------------------Change Password----------------------\n")

    loginId = input("Enter the LoginId:")
    Password = input("Enter the New Password:")
    sql = "UPDATE employee SET empPassword = %s WHERE empLoginId = %s"
    value = (Password, loginId)
    cursor.execute(sql, value)
    print("PASSWORD CHANGED!!!!!")

    db.commit()
    db.close()


# ***************************************** MAIN MENU *****************************************
def expert_module_main_menu():

    print("\n+-------------EXPERT MODULE--------------+")
    print("|1. View Assigned Bug                    |")
    print("|2. Filter Assigned Bugs based on status |")
    print("|3. Solve the Bug                        |")
    print("|4. Change Password                      |")
    print("|5. Exit                                 |")
    print("+----------------------------------------+")

    choice = int(input("\nEnter your choice(1-5):"))

    if choice == 1:
        view_assigned_bugs()
        expert_module_main_menu()
    elif choice == 2:
        filter_Assigned_Bugs_based_on_status()
        expert_module_main_menu()
    elif choice == 3:
        solve_the_Bug()
        expert_module_main_menu()
    elif choice == 4:
        expert_Change_Password()
        expert_module_main_menu()
    elif choice == 5:
        print("EXIT!!!")
        return

    else:
        print("INVALID CHOICE!!!!")


expert_module_main_menu()
