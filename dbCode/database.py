from dbCode import *
from dbCode.database import database


def runProgram():
    # interface
    db = database()
    while True:
        print(
            "Welcome. Please select an option\n(1) Show database\n(2) Insert new item\n(3) Update email\n(4) Delete student\n(5) Exit")
        ini = input("What do you want to do? ")
        #show database
        if ini == "1":
            db.getAllStudents()
        #Insert new item
        elif ini == "2":
            fname = input("First name: ")
            lname = input("Last name: ")
            email = input("Email: ")
            date = input("Enrollment date: ")
            db.addStudent(fname, lname, email, date)
        #update email
        elif ini == "3":
            idstu = input("Which student id: ")
            newemail = input("New email: ")
            db.updateStudentEmail(idstu, newemail)
        #delete item
        elif ini == "4":
            delid = input("Which student id: ")
            db.deleteStudent(delid)
        #exit
        elif ini == "5":
            break
        print("\n")

runProgram()
