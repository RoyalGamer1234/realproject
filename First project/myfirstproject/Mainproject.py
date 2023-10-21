import mysql.connector
Database = mysql.connector.connect(host='localhost', user='root', password='', database='project')
def entries():
    cur = Database.cursor()
    fn = input("Enter First Name\n")
    ln = input("Enter Last Name\n")
    mn = input("Insert Mobile Number\n")
    dat = input("Insert Entry Date and Time(Please enter in format of YYYY-MM-DD and HH:MM:SS)\n")
    guestEntry(fn, ln, mn, dat)
    loop = input("Do you wish to start again\n")
    if loop == "Yes" or loop == "yes":
        entries()
    else:
        print("Program Ended")

def guestEntry(fName, lName, mobileNumber, dateOfBirth):
    cur = Database.cursor()
    s = "Insert into Entries (FirstName, LastName, MobileNumber, Dateandtime) Values(%s,%s,%s,%s)"
    t = (fName, lName, mobileNumber, dateOfBirth)
    cur.execute(s,t)
    Database.commit()

entries()