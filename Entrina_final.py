import sqlite3
print"note: it's already in <.db>, no need to include it in your db name"
db_name = raw_input("Enter your database name:") + '.db'

conn = sqlite3.connect(db_name)
c = conn.cursor()

class Student (object):

    def __init__(self, firstName,middleInit, lastName, idNum, Course):
        self.firstName=firstName
        self.middleInit=middleInit
        self.lastName=lastName
        self.idNum=idNum
        self.course=Course



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS studentRecord(FirstName TEXT, MiddleInitial TEXT, LastName TEXT, ID TEXT, Course TEXT)')

def add_entry(student):
    c.execute("INSERT INTO studentRecord (FirstName, MiddleInitial, LastName, ID, Course) VALUES (?,?,?,?,?)",
        (student.firstName,student.middleInit, student.lastName,student.idNum,student.course))
    conn.commit()

def delete_entry():
    idnum = raw_input("Enter the ID: ")
    c.execute("DELETE FROM studentRecord WHERE ID = ?", (idnum,))
    conn.commit()

def search_entry():
    select = raw_input("Please enter the ID Number: ")
    c.execute("SELECT * FROM studentRecord where ID = ?", (select,))
    for row in c.fetchall():
        print (row)

def update_entry():
    select = raw_input("Enter the ID:")
    choice = raw_input("What to update? \n~First name\n~Last name\n~MI\n~Id no\n~Course\n")
    if choice == "First name":
        change = raw_input("Enter new first name: ")
        conn.execute("UPDATE studentRecord set FirstName = ? where ID = ?", (change,select,))
        conn.commit()
    elif choice == "Last name":
        change = raw_input("Enter new last name: ")
        conn.execute("UPDATE studentRecord set LastName = ? where ID = ?", (change,select,))
        conn.commit()
    elif choice == "MI":
        change = raw_input("Enter new middle initial: ")
        conn.execute("UPDATE studentRecord set MiddleInitial = ? where ID = ?", (change,select,))
        conn.commit()
    elif choice == "Id no":
        change = raw_input("Enter the new id number: ")
        conn.execute("UPDATE studentRecord set ID = ? where ID = ?", (change, select,))
        conn.commit()
    elif choice == "Course":
        change = raw_input("Enter new course: ")
        conn.execute("UPDATE studentRecord set Course = ? where ID = ?", (change,select,))
        conn.commit()

def sort_entry():
    choice = raw_input("Sort it by? \nLast name, ID num, Course: \n")

    if choice == "Last name":
        c.execute("SELECT * FROM studentRecord ORDER BY LastName ASC")
        for row in c.fetchall():
            print(row)
        conn.commit()
    if choice == "ID num":
        c.execute("SELECT * FROM studentRecord ORDER BY ID ASC")
        for row in c.fetchall():
            print(row)
        conn.commit()
    if choice == "Course":
        c.execute("SELECT*FROM studentRecord ORDER BY Course ASC")
        for row in c.fetchall():
            print(row)
        conn.commit()

def prints():
    c.execute("SELECT * FROM studentRecord")
    for row in c.fetchall():
        print row




def main():
    create_table()
    prints()
    while(True):

        option = raw_input("Please choose the operation you want to perform (ADD, DELETE, UPDATE, SORT, SEARCH): ")
        if option == "ADD":
            fn = raw_input("first name: ")
            mi = raw_input("middle initial: ")
            ln = raw_input("last name: ")
            idn = raw_input("id num: ")
            course = raw_input("course:")
            student = Student(fn, mi, ln, idn, course)
            add_entry(student)
        if option == "DELETE":
            delete_entry()
        if option == "SEARCH":
            search_entry()
        if option == "UPDATE":
            update_entry()
        if option == "SORT":
            sort_entry()

        opt2 = raw_input("EXIT? Y/N: ")
        if opt2 == "Y":
            break


    prints()
    c.close()
    conn.close()


if __name__ == '__main__':
    main()